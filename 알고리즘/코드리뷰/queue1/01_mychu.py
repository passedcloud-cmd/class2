# ------------------------------------------------------------
# 02. 큐 활용 - "마이쮸를 나눠주자"
# ------------------------------------------------------------
# [문제]
#   담임 선생님이 학생들에게 마이쮸를 나눠준다. 마지막 마이쮸를 받는 학생은 몇 번일까?
#
# [진행 규칙]
#   1. 초기 마이쮸는 총 20개.
#   2. 1번 학생이 1개를 받기 위해 줄을 서면서 시작.
#   3. 줄의 맨 앞 학생이 나와서 자신이 받기로 한 개수만큼 받는다.
#   4. 받은 학생은 '다음에 받을 개수'를 1개 늘려서 다시 줄 맨 뒤로 간다.
#   5. 그 직후, 아직 줄 선 적 없는 새 학생이 1개를 받기 위해 줄 맨 뒤에 선다.
#   6. 남은 개수가 학생이 받으려는 개수보다 부족하면, 그 학생이 남은 걸 다 가져가고 종료.
#
# [학습 목표] 이 문제는 "규칙을 코드로 옮기는 것"이 전부다.
#        규칙 3번(맨 앞에서 꺼냄) = dequeue, 규칙 4·5번(맨 뒤에 세움) = enqueue.
#        큐를 쓰는 순간 '순서 관리'를 자료구조가 대신 해 준다.
#
# [비유] 놀이공원 자유이용권 재입장
#        타고 나온 사람이 다시 줄 맨 뒤에 서고, 새로 온 손님도 그 뒤에 선다.
#
# [준비물] 파이썬 리스트 하나면 충분하다.
#   맨 뒤에 넣기 = append(x),  맨 앞에서 꺼내기 = pop(0)
#   이 pop(0) 이 왜 문제가 되는지는 02번에서, 그 해결책은 04번에서 다룬다.
# ------------------------------------------------------------


def mychu_simulation(total_candy):
    # 큐 초기화: (학생 번호, 이번에 받을 사탕 수)
    queue = [(1, 1)]

    last_student = 0  # 마지막으로 받은 학생 번호
    next_student = 2  # 다음에 줄 설 학생 번호

    print(f'=== 마이쮸 {total_candy}개 나누기 시작 ===')

    while total_candy > 0:
        # TODO 1) 큐의 맨 앞 학생을 꺼내세요. (Dequeue)
        #   힌트: 리스트의 맨 앞을 꺼내는 메서드는 pop(0) 이다.
        #         큐에는 (학생번호, 받을개수) 튜플이 들어 있다.
        student_id, want = queue.pop(0)

        # TODO 2) 실제로 줄 사탕 개수를 정하세요.
        #   힌트: 원하는 만큼 주되, 남은 게 부족하면 남은 만큼만 준다.
        #         두 값 중 작은 쪽을 고르는 내장 함수가 있다.
        give = min(want, total_candy)

        total_candy -= give
        last_student = student_id # 마지막 학생을 찾아야 하므로 갱신해야 함

        # [무한 루프 방지] TODO 를 채우기 전에는 give 가 0이라 사탕이 줄지 않는다.
        # TODO 1, 2 를 채우고 나면 give 는 항상 1 이상이므로 이 분기는 실행되지 않는다.
        # if give == 0:
        #     print('(아직 TODO 1, 2 를 채우지 않아 사탕이 줄지 않습니다)')
        #     break

        print(f'{student_id}번 학생이 {give}개 받음 (남은 개수: {total_candy})')

        # 사탕이 다 떨어졌으면 종료
        if total_candy == 0:
            break

        # TODO 3) 받은 학생은 '받을 개수'를 1개 늘려서 다시 줄 맨 뒤로 갑니다. (Enqueue)
        queue.append((student_id, want + 1))

        # TODO 4) 새로운 학생이 줄 맨 뒤에 섭니다. (항상 1개부터 시작)
        #   [순서 주의] 재입장(TODO 3)이 먼저, 신규 입장(TODO 4)이 나중이다.
        queue.append((next_student, 1))

        next_student += 1

    print(f'마지막 사탕의 주인공은 {last_student}번 학생입니다!')
    return last_student


# --- 실행 ---
answer = mychu_simulation(20)
print(f'\n정답 확인: {answer}번 (기대값 2번)')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] 단계마다 대기열이 어떻게 바뀌는지 보기
# ------------------------------------------------------------
def trace_mychu(total_candy):
    """노션 문서의 단계별 표를 그대로 재현"""
    queue = [(1, 1)]
    next_student = 2
    step = 0

    def show(items):
        """대기열이 길어지면 앞쪽 4명만 보여준다"""
        head = ', '.join(f'({sid},{cnt})' for sid, cnt in items[:4])
        tail = f' ... 총 {len(items)}명' if len(items) > 4 else ''
        return f'[{head}]{tail}'

    print(f'  {"단계":<9} {"남은":>5}  {"대기열 (학생번호, 받을 개수)":<44} {"다음 입장"}')
    print(f'  {"-" * 9} {"-" * 5}  {"-" * 44} {"-" * 9}')
    print(f'  {"시작":<9} {total_candy:>5}  {show(queue):<44} {next_student}')

    while total_candy > 0:
        step += 1
        student_id, want = queue.pop(0)

        give = min(want, total_candy)
        total_candy -= give

        if total_candy == 0:
            print(f'  {f"{step}차 분배":<9} {total_candy:>5}  '
                  f'{student_id}번이 {give}개 받고 소진 -> 종료')
            print(f'\n  마지막 사탕의 주인공: {student_id}번 학생')
            break

        queue.append((student_id, want + 1))
        queue.append((next_student, 1))
        next_student += 1

        print(f'  {f"{step}차 분배":<9} {total_candy:>5}  {show(queue):<44} {next_student}')


print('=== 단계별 대기열 변화 ===')
trace_mychu(20)

# [읽는 법]
#   1차 분배: 1번이 1개 받고 (1,2)로 재입장, 그 뒤에 2번이 (2,1)로 신규 입장
#   2차 분배: 다시 1번 차례... 가 아니라 큐 맨 앞은 (1,2) 다.
#             받은 사람이 뒤로 갔으므로 (1,2), (2,1) 순서로 서 있다.
#   => 순서를 머리로 계산하지 않아도, 큐에 넣고 빼기만 하면 알아서 맞는다.


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [실험] 사탕 개수를 바꾸면 정답도 바뀔까?
# ------------------------------------------------------------
def mychu_quiet(total_candy):
    """출력 없이 마지막 학생 번호만 반환"""
    queue = [(1, 1)]
    last_student = 0
    next_student = 2

    while total_candy > 0:
        student_id, want = queue.pop(0)
        give = min(want, total_candy)
        total_candy -= give
        last_student = student_id

        if total_candy == 0:
            break

        queue.append((student_id, want + 1))
        queue.append((next_student, 1))
        next_student += 1

    return last_student


print('=== 사탕 개수별 마지막 주인공 ===')
print(f'  {"사탕 개수":>10} | {"마지막 학생":>10}')
print(f'  {"-" * 10} | {"-" * 10}')
for candy in [5, 10, 20, 50, 100]:
    print(f'  {candy:>10} | {mychu_quiet(candy):>10}번')

# [포인트] 규칙이 조금 복잡해 보여도, 손으로 풀기 어려운 것을
#          컴퓨터는 시뮬레이션으로 그냥 밀어붙여 답을 낸다.
#          이것이 '완전 탐색 / 시뮬레이션' 유형의 기본 발상이다.


print('\n' + '=' * 66 + '\n')
