# =====================================================================
#  배틀싸피 연습용 간이 시뮬레이터 (게임 없이 내 AI를 콘솔에서 테스트)
#  매뉴얼 규칙대로 만들었지만 진짜 게임과 100% 같지는 않을 수 있음!
#
#  사용법:  python simulator.py
#  (tank_ai.py 와 같은 폴더에 두고 실행)
# =====================================================================
import random

from tank_ai import TankAI

DIRS = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
WORDS = ['BATTLESSAFY', 'SAMSUNG', 'ALGORITHM', 'PYTHON', 'MISSILE', 'TANK',
         'HELLO', 'WORLD', 'VICTORY', 'ATTACK', 'DEFENSE', 'STRATEGY',
         'COMPUTER', 'SCIENCE', 'KOREA', 'SEOUL', 'GWANGJU', 'DAEJEON', 'BUSAN']


class Simulator:
    def __init__(self, map_text, normal=1, mega=0, x_hp=10, shift=17,
                 words=None, max_turns=100, seed=0):
        self.grid = [row.split() for row in map_text.strip().splitlines()]
        self.H, self.W = len(self.grid), len(self.grid[0])
        for r in range(self.H):
            for c in range(self.W):
                if self.grid[r][c] == 'M':
                    self.pos = (r, c)
                    self.grid[r][c] = 'G'          # 탱크 밑의 땅
                elif self.grid[r][c] == 'X':
                    self.target = (r, c)
        self.hp, self.dir = 100, 'R'
        self.normal, self.mega, self.x_hp = normal, mega, x_hp
        self.shift, self.words = shift, words or WORDS
        self.rng = random.Random(seed)
        self.turn, self.max_turns = 0, max_turns
        self.result = None          # 'SUCCESS' / 'FAILED'
        self.warnings = []
        self.answers = []

    # ----- 서버가 보내주는 문자열 만들기 -----
    def game_data(self):
        r0, c0 = self.pos
        self.answers = []
        for dr, dc in DIRS.values():
            r, c = r0 + dr, c0 + dc
            if 0 <= r < self.H and 0 <= c < self.W and self.grid[r][c] == 'F':
                self.answers.append(self.rng.choice(self.words))
        codes = [''.join(chr((ord(ch) - 65 + self.shift) % 26 + 65) for ch in w)
                 for w in self.answers]
        rows = []
        for r in range(self.H):
            row = list(self.grid[r])
            if r == r0:
                row[c0] = 'M'
            rows.append(' '.join(row))
        lines = [f'{self.H} {self.W} 1 1 {len(codes)}'] + rows
        lines += [f'M {self.hp} {self.dir} {self.normal} {self.mega}', f'X {self.x_hp}']
        lines += codes
        return '\n'.join(lines) + '\n'

    # ----- 명령 처리 -----
    def step(self, cmd):
        self.turn += 1
        t = cmd.split()
        if t and t[0] in DIRS and len(t) >= 2:
            self.dir = t[0]
            t = t[1:]
        if not t:
            self.warnings.append(f'턴{self.turn}: 빈 명령')
        elif t[0] == 'A':
            self._move()
        elif t[0] == 'F':
            self._fire(mega=(len(t) > 1 and t[1] == 'M'))
        elif t[0] == 'G':
            guess = t[1] if len(t) > 1 else ''
            if guess in self.answers and self.mega < 10:
                self.mega += 1
            else:
                self.warnings.append(f'턴{self.turn}: 해독 실패 ({guess})')
        elif t[0] != 'S':
            self.warnings.append(f'턴{self.turn}: 모르는 명령 {cmd}')

        if self.x_hp <= 0:
            self.result = 'SUCCESS'
        elif self.hp <= 0 or self.turn >= self.max_turns:
            self.result = 'FAILED'

    def _move(self):
        dr, dc = DIRS[self.dir]
        r, c = self.pos[0] + dr, self.pos[1] + dc
        if 0 <= r < self.H and 0 <= c < self.W and self.grid[r][c] in ('G', 'S'):
            self.pos = (r, c)
            if self.grid[r][c] == 'S':
                self.hp -= 10
        else:
            self.warnings.append(f'턴{self.turn}: 이동 불가 칸으로 이동 시도')

    def _fire(self, mega):
        if mega and self.mega == 0 or (not mega and self.normal == 0):
            self.warnings.append(f'턴{self.turn}: 포탄 없이 발사')
            return
        if mega:
            self.mega -= 1
        else:
            self.normal -= 1
        dr, dc = DIRS[self.dir]
        for k in range(1, 4):
            r, c = self.pos[0] + dr * k, self.pos[1] + dc * k
            if not (0 <= r < self.H and 0 <= c < self.W):
                return
            cell = self.grid[r][c]
            if cell in ('G', 'S', 'W'):
                continue
            if cell == 'T':
                self.grid[r][c] = 'G'
            elif cell == 'X':
                self.x_hp -= 70 if mega else 30
            return                                  # 처음 맞은 대상에서 멈춤

    def show(self):
        for r in range(self.H):
            row = list(self.grid[r])
            if r == self.pos[0]:
                row[self.pos[1]] = 'M'
            print(' '.join(row))


def play(sim, ai, verbose=False):
    while sim.result is None:
        data = sim.game_data()
        cmd = ai.decide(data)
        sim.step(cmd)
        if verbose:
            print(f'--- 턴 {sim.turn}: {cmd}')
            sim.show()
    return sim.result, sim.turn


STAGE1 = """
G G G G G G G G
G G G G G G G G
R R R R R R G G
R R R G X R G G
R R G G R R G G
R G G R R R G G
M G R R R R G G
R R R R R R G G
"""

if __name__ == '__main__':
    sim = Simulator(STAGE1, normal=1, mega=0, x_hp=10)
    result, turns = play(sim, TankAI(memory_file='sim_memory.json'), verbose=True)
    print(f'\n결과: {result} ({turns}턴)')
