# =====================================================================
#  배틀싸피 탱크 AI  (스테이지 모드 1~6용, Python)
#
#  [붙여넣는 위치]
#   1) 이 파일 내용 전체를 main.py 의
#      "알고리즘 함수/메서드 부분 구현 시작" ~ "끝" 주석 사이에 붙여넣기
#   2) while 반복문 안의 "알고리즘 메인 부분" 을 아래 두 줄로 바꾸기
#          output = tank_ai.decide(game_data)
#          game_data = submit(output)
#
#  [이 AI가 매 턴 하는 일]
#   - 서버가 보내준 game_data 를 직접 읽어서(파싱) 지금 상황을 파악하고
#   - "포탑을 부수기까지 남은 턴 수" 가 가장 적은 계획을 새로 세운 뒤
#   - 그 계획의 '첫 번째 행동' 하나만 명령으로 돌려줌
#   매 턴 새로 계획하니까, 맵이 바뀌어도(나무가 부서지는 등) 알아서 따라감.
# =====================================================================
import heapq
import json
import math
import os


class TankAI:
    # 방향 이름 -> (행 변화, 열 변화).  U=위, D=아래, L=왼쪽, R=오른쪽
    DIRS = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

    NORMAL_DAMAGE = 30      # 일반 포탄 데미지
    MEGA_DAMAGE = 70        # 메가 포탄 데미지
    FIRE_RANGE = 3          # 포탄 사거리 (3칸)
    MAX_MEGA = 10           # 메가 포탄 최대 보관 개수

    WALKABLE = ('G', 'S')           # 탱크가 올라설 수 있는 칸 (풀, 모래)
    SHELL_PASS = ('G', 'S', 'W')    # 포탄이 그냥 통과하는 칸 (지형은 다 통과)
    SAND_EXTRA = 0.2                # 모래는 체력이 깎이니까 살짝 덜 선호

    # 매뉴얼 예시: 암호문 SRKKCVJJRWP -> 해독문 BATTLESSAFY
    # S(18) - B(1) = 17 이니까 "알파벳을 17칸씩 밀어서" 암호화한 것.
    MANUAL_SHIFT = 17

    # 영어 알파벳 등장 빈도(%) - 해독 결과가 '영어처럼 보이는지' 점수 매길 때 사용
    ENGLISH_FREQ = {
        'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23,
        'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03,
        'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99,
        'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
        'Y': 1.97, 'Z': 0.07,
    }
    HINT_WORDS = ('SSAFY', 'SAMSUNG', 'BATTLE', 'TANK', 'MISSILE', 'MEGA',
                  'ATTACK', 'FIRE', 'CODE', 'HELLO', 'WORLD', 'PYTHON',
                  'JAVA', 'KOREA', 'SEOUL', 'ALGORITHM', 'SOFTWARE', 'ACADEMY')

    def __init__(self, memory_file=None):
        if memory_file is None:
            try:
                base_dir = os.path.dirname(os.path.abspath(__file__))
            except NameError:
                base_dir = os.getcwd()
            memory_file = os.path.join(base_dir, 'tank_memory.json')
        self.memory_file = memory_file
        self.known_shift = self._load_shift()   # 한 번 맞춘 암호 간격은 기억해 둠
        self.bad_shifts = set()                  # 틀렸던 간격 목록
        self.last_decode = None                  # 직전 턴에 해독을 시도했는지 기록

    # =================================================================
    # 1. 매 턴 호출되는 메인 함수
    # =================================================================
    def decide(self, game_data):
        """game_data(서버가 보낸 문자열)를 받아서 이번 턴 명령 문자열을 돌려줌."""
        try:
            st = self.parse(game_data)
        except Exception as e:                   # 혹시 모를 오류로 연결이 끊기면 실패니까 방어
            print('[AI] 데이터 읽기 실패:', e)
            return 'S'
        if st is None:
            return 'S'

        self._check_last_decode(st)

        try:
            cmd = self.choose_command(st)
        except Exception as e:
            print('[AI] 계산 중 오류, 이번 턴은 대기:', e)
            cmd = 'S'
        print(f"[AI] 위치 {st['me']}, 포탄 {st['normal']}/메가 {st['mega']}, "
              f"포탑 체력 {st['target_hp']} -> 명령: {cmd}")
        return cmd

    # =================================================================
    # 2. 입력 데이터 읽기 (파싱)
    # =================================================================
    def parse(self, game_data):
        if not game_data:
            return None
        if isinstance(game_data, bytes):
            game_data = game_data.decode('utf-8')
        lines = [ln.strip() for ln in game_data.strip().splitlines() if ln.strip()]

        head = [int(x) for x in lines[0].split()]
        while len(head) < 5:
            head.append(0)
        H, W, n_ally, n_enemy, n_code = head[:5]

        grid = [lines[1 + i].split() for i in range(H)]
        idx = 1 + H
        ally_lines = lines[idx: idx + n_ally]
        idx += n_ally
        enemy_lines = lines[idx: idx + n_enemy]
        idx += n_enemy
        codes = [ln.replace(' ', '') for ln in lines[idx: idx + n_code]]

        st = {'H': H, 'W': W, 'me': None, 'target': None, 'supply': [],
              'hp': 100, 'dir': 'R', 'normal': 0, 'mega': 0,
              'target_hp': 1, 'codes': codes}

        for tokens in (ln.split() for ln in ally_lines):
            if tokens[0] == 'M' and len(tokens) >= 5:
                st['hp'] = int(tokens[1])
                st['dir'] = tokens[2]
                st['normal'] = int(tokens[3])
                st['mega'] = int(tokens[4])
        for tokens in (ln.split() for ln in enemy_lines):
            if tokens[0] == 'X' and len(tokens) >= 2:
                st['target_hp'] = int(tokens[1])

        for r in range(H):
            for c in range(len(grid[r])):
                cell = grid[r][c]
                if cell == 'M':
                    st['me'] = (r, c)
                elif cell == 'X':
                    st['target'] = (r, c)
                elif cell == 'F':
                    st['supply'].append((r, c))

        # 계획 세울 때는 내 탱크가 서 있는 칸을 '빈 땅(G)'으로 취급
        if st['me'] is not None:
            grid[st['me'][0]][st['me'][1]] = 'G'
        st['grid'] = grid
        return st

    # =================================================================
    # 3. 이번 턴에 할 행동 고르기
    # =================================================================
    def choose_command(self, st):
        if st['me'] is None or st['target'] is None:
            return 'S'
        plan = self.make_plan(st)
        if plan is None:
            return self.fallback(st)

        cost, kind, goal_state, info, parent = plan
        step = self._first_step(parent, goal_state)

        if step is None:
            # 이미 계획한 위치에 도착함
            if kind == 'attack':
                return self._fire_command(st, info)        # info = 포탑 쪽 방향
            return self._decode_command(st)                 # 보급시설 옆 → 암호 해독

        d, (nr, nc, _) = step
        if st['grid'][nr][nc] == 'T':
            return self._fire_command(st, d)                # 길을 막은 나무부터 부수기
        return d + ' A'                                     # 한 칸 이동

    # -----------------------------------------------------------------
    # 가장 턴이 적게 드는 계획 찾기
    #   계획 A: (필요하면 나무를 부수며) 사격 위치로 이동 → 포탑에 발사
    #   계획 B: 보급시설 옆으로 이동 → 암호 해독 k번 → 사격 위치로 이동 → 발사
    # -----------------------------------------------------------------
    def make_plan(self, st):
        grid, me = st['grid'], st['me']
        n, m, hp_x = st['normal'], st['mega'], st['target_hp']
        spots = self._fire_spots(grid, st['target'])
        if not spots:
            return None

        max_t0 = n + m
        dist0, par0 = self._dijkstra(grid, me, max_t0, st['hp'])
        best = None

        # ---- 계획 A: 바로 공격 ----
        for (pr, pc), fdir, line_trees in spots:
            for t in range(max_t0 + 1):
                d = dist0.get((pr, pc, t))
                if d is None:
                    continue
                shots = self._shots_needed(n, m, t + line_trees, hp_x)
                if shots is None:
                    continue
                cost = d + line_trees + shots
                if best is None or cost < best[0]:
                    best = (cost, 'attack', (pr, pc, t), fdir, par0)

        # ---- 계획 B: 보급시설에서 메가 포탄 챙기고 공격 ----
        if st['supply'] and m < self.MAX_MEGA:
            per_decode = 1 if self.known_shift is not None else 2   # 간격을 모르면 틀릴 수도 있으니 넉넉히
            for q in self._supply_cells(st):
                dist_q = None
                for t1 in range(max_t0 + 1):
                    d1 = dist0.get((q[0], q[1], t1))
                    if d1 is None:
                        continue
                    use_n = min(t1, n)
                    n1, m1 = n - use_n, m - (t1 - use_n)
                    if m1 < 0:
                        continue
                    if dist_q is None:
                        dist_q, _ = self._dijkstra(grid, q, n + self.MAX_MEGA, st['hp'])
                    for (pr, pc), fdir, line_trees in spots:
                        for t2 in range(n1 + self.MAX_MEGA + 1):
                            d2 = dist_q.get((pr, pc, t2))
                            if d2 is None:
                                continue
                            for k in range(1, self.MAX_MEGA - m1 + 1):
                                shots = self._shots_needed(n1, m1 + k, t2 + line_trees, hp_x)
                                if shots is None:
                                    continue
                                cost = d1 + k * per_decode + d2 + line_trees + shots
                                if best is None or cost < best[0]:
                                    best = (cost, 'supply', (q[0], q[1], t1), k, par0)
                                break
        return best

    # -----------------------------------------------------------------
    # 다익스트라 최단 경로
    #   상태 = (행, 열, 지금까지 부순 나무 수)
    #   풀 칸 이동 = 1턴, 나무 칸 = 쏘고(1턴) + 이동(1턴) = 2턴 & 포탄 1개
    # -----------------------------------------------------------------
    def _dijkstra(self, grid, start, max_trees, hp):
        H = len(grid)
        s = (start[0], start[1], 0)
        dist = {s: 0}
        parent = {}
        pq = [(0, s)]
        while pq:
            d, cur = heapq.heappop(pq)
            if d > dist[cur]:
                continue
            r, c, t = cur
            for dname, (dr, dc) in self.DIRS.items():
                nr, nc = r + dr, c + dc
                if not (0 <= nr < H and 0 <= nc < len(grid[nr])):
                    continue
                cell = grid[nr][nc]
                if cell == 'G':
                    step, nt = 1, t
                elif cell == 'S':
                    if hp <= 10:
                        continue
                    step, nt = 1 + self.SAND_EXTRA, t
                elif cell == 'T':
                    if t >= max_trees:
                        continue
                    step, nt = 2, t + 1
                else:
                    continue                    # 물, 바위, 보급시설, 다른 유닛은 못 지나감
                nd = d + step
                ns = (nr, nc, nt)
                if nd < dist.get(ns, math.inf):
                    dist[ns] = nd
                    parent[ns] = (cur, dname)
                    heapq.heappush(pq, (nd, ns))
        return dist, parent

    def _first_step(self, parent, goal_state):
        """목표 상태에서 거꾸로 따라가서 '첫 번째로 들어갈 칸'과 방향을 구함."""
        cur, step = goal_state, None
        while cur in parent:
            prev, d = parent[cur]
            step = (d, cur)
            cur = prev
        return step

    # -----------------------------------------------------------------
    # 포탑을 쏠 수 있는 위치 목록
    #   포탑과 같은 줄(가로/세로)이고 거리 1~3, 사이에 바위 등이 없어야 함.
    #   사이에 나무가 있으면 그 수만큼 먼저 쏴서 치워야 함.
    # -----------------------------------------------------------------
    def _fire_spots(self, grid, target):
        H = len(grid)
        xr, xc = target
        spots = []
        for fdir, (dr, dc) in self.DIRS.items():
            trees_between = 0
            for k in range(1, self.FIRE_RANGE + 1):
                pr, pc = xr - dr * k, xc - dc * k   # 여기서 fdir 방향으로 쏘면 포탑에 닿음
                if not (0 <= pr < H and 0 <= pc < len(grid[pr])):
                    break
                cell = grid[pr][pc]
                if cell in self.WALKABLE or cell == 'T':
                    spots.append(((pr, pc), fdir, trees_between))
                if cell == 'T':
                    trees_between += 1
                elif cell not in self.SHELL_PASS:
                    break                          # 바위/보급시설/다른 탱크가 포탄을 막음
        return spots

    def _supply_cells(self, st):
        """보급시설과 상하좌우로 붙어 있는 칸 = 암호 해독 가능한 자리"""
        grid, cells = st['grid'], set()
        for fr, fc in st['supply']:
            for dr, dc in self.DIRS.values():
                r, c = fr + dr, fc + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    if grid[r][c] in self.WALKABLE or grid[r][c] == 'T':
                        cells.add((r, c))
        if st['me'] in cells and not st['codes']:
            cells.discard(st['me'])               # 붙어 있는데 암호문이 안 왔으면 제외
        return sorted(cells)

    def _shots_needed(self, normal, mega, trees, hp_x):
        """나무 trees개를 치우고 포탑(체력 hp_x)을 부수는 데 필요한 '포탑 사격 횟수'.
        포탄이 모자라면 None.  나무는 일반 포탄부터, 포탑은 메가 포탄부터 쓰는 게 이득."""
        use_n = min(trees, normal)
        use_m = trees - use_n
        if use_m > mega:
            return None
        normal -= use_n
        mega -= use_m
        shots = 0
        while hp_x > 0 and mega > 0:
            hp_x -= self.MEGA_DAMAGE
            mega -= 1
            shots += 1
        while hp_x > 0 and normal > 0:
            hp_x -= self.NORMAL_DAMAGE
            normal -= 1
            shots += 1
        return shots if hp_x <= 0 else None

    # =================================================================
    # 4. 명령 만들기
    # =================================================================
    def _fire_command(self, st, d):
        """d 방향으로 발사. 맞을 대상이 나무인지 포탑인지 보고 포탄 종류를 고름."""
        grid, (r, c) = st['grid'], st['me']
        dr, dc = self.DIRS[d]
        first_hit = None
        for k in range(1, self.FIRE_RANGE + 1):
            nr, nc = r + dr * k, c + dc * k
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[nr])):
                break
            if grid[nr][nc] not in self.SHELL_PASS:
                first_hit = grid[nr][nc]
                break
        n, m = st['normal'], st['mega']
        if first_hit == 'X':
            # 포탑: 일반 포탄 한 방이면 충분하면 일반, 아니면 메가부터
            use_mega = m > 0 and not (st['target_hp'] <= self.NORMAL_DAMAGE and n > 0)
        else:
            # 나무 등: 일반 포탄부터 사용 (메가는 포탑용으로 아껴 둠)
            use_mega = n == 0 and m > 0
        return f'{d} F M' if use_mega else f'{d} F'

    def _decode_command(self, st):
        cipher = st['codes'][0].upper()
        shift = self._pick_shift(cipher)
        plain = self._caesar_decode(cipher, shift)
        self.last_decode = (shift, st['mega'], st['H'], st['W'])
        return 'G ' + plain

    def fallback(self, st):
        """계획을 못 세웠을 때(포탄이 부족한데 보급시설도 없는 등)의 대비책."""
        if st['codes'] and st['mega'] < self.MAX_MEGA:
            return self._decode_command(st)
        # 포탑에 가장 가까워지는 칸 쪽으로라도 이동
        dist, parent = self._dijkstra(st['grid'], st['me'], 0, st['hp'])
        tr, tc = st['target']
        goal = min(dist, key=lambda s: (abs(s[0] - tr) + abs(s[1] - tc), dist[s]))
        step = self._first_step(parent, goal)
        return 'S' if step is None else step[0] + ' A'

    # =================================================================
    # 5. 카이사르 암호 해독
    # =================================================================
    @staticmethod
    def _caesar_decode(cipher, shift):
        out = []
        for ch in cipher:
            if 'A' <= ch <= 'Z':
                out.append(chr((ord(ch) - 65 - shift) % 26 + 65))
            else:
                out.append(ch)
        return ''.join(out)

    def _english_score(self, text):
        score = sum(math.log(self.ENGLISH_FREQ.get(ch, 0.05)) for ch in text if 'A' <= ch <= 'Z')
        for w in self.HINT_WORDS:
            if w in text:
                score += 2 * len(w)
        return score

    def _pick_shift(self, cipher):
        """기억해 둔 간격이 있으면 그걸 쓰고, 없으면 26가지를 다 풀어서 가장 영어 같은 것 선택."""
        if self.known_shift is not None:
            return self.known_shift
        if len(self.bad_shifts) >= 26:
            self.bad_shifts.clear()
        best_shift, best_score = None, -math.inf
        for s in range(26):
            if s in self.bad_shifts:
                continue
            score = self._english_score(self._caesar_decode(cipher, s))
            if s == self.MANUAL_SHIFT:
                score += 1.5                     # 매뉴얼 예시 간격에 살짝 가산점
            if score > best_score:
                best_shift, best_score = s, score
        return best_shift

    def _check_last_decode(self, st):
        """직전 턴에 해독을 시도했다면, 메가 포탄이 늘었는지 보고 정답/오답 판정."""
        if self.last_decode is None:
            return
        shift, mega_before, h, w = self.last_decode
        self.last_decode = None
        if (st['H'], st['W']) != (h, w):
            return                               # 스테이지가 바뀐 경우는 판정 안 함
        if st['mega'] > mega_before:
            if self.known_shift != shift:
                print(f'[AI] 암호 간격 {shift} 정답! 기억해 둘게.')
                self.known_shift = shift
                self._save_shift(shift)
            self.bad_shifts.clear()
        else:
            print(f'[AI] 암호 간격 {shift} 은(는) 틀림.')
            self.bad_shifts.add(shift)
            if self.known_shift == shift:
                self.known_shift = None

    def _load_shift(self):
        try:
            with open(self.memory_file, encoding='utf-8') as f:
                return int(json.load(f)['shift'])
        except Exception:
            return None

    def _save_shift(self, shift):
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump({'shift': shift}, f)
        except Exception:
            pass


tank_ai = TankAI()
