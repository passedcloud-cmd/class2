import sys
sys.stdin = open("15기-수열나머지합.txt")
T = int(input())
for test_case in range(1, T + 1):
	# N은 원소 개수
	N = int(input())

	# 수열 arr
	arr = list(map(int, input().split()))

	# 나누기 후 나머지의 합계는 0으로 시작
	count_number = 0

	# i가 첫 번째 수: 0부터 (N - 2)번까지 순회. 두 개씩 선택하기 때문임.
	for i in range(0, N - 1):
		# j가 두 번째 수: (i + 1)부터 (N - 1)번까지 순회.
		for j in range(i + 1, N):
			# 숫자를 2개 골랐으면 arr[i]를 arr[j]로 나눈 나머지와 arr[j]를 arr[i]로 나눈 나머지를 구하여 누적 합.
			count_number += (arr[i] % arr[j])
			count_number += (arr[j] % arr[i])

	print(f'#{test_case} {count_number}')

# 입력
# 2
# 3
# 3 5 3
# 4
# 3 7 5 8

# 출력
# #1 10
# #2 37