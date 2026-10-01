# # 10진수 17을 3진수로 바꾸기
# a=17
# trans=''
# while a != 0:
#     rest = a % 3
#     trans += str(rest)
#     a //= 3
# answer = trans[::-1]
# print(answer)
#
# # 다시 10진법으로
# result = int(answer, 3)
# print(result)

# print(13&9) # empersand # and
# print(13|9) # vertical bar # or
# print(13^9) # caret #xor
# print(10<<2) # 이진법에서 2칸씩 왼쪽 이동. 10 * 2^2 = 40
# print(10>>2) # 이진법에서 2칸씩 오른쪽 이동. 10 // 2^2 = 2
#
# arr = [1,2,3]
# for i in range(1<<3): # 부분집합의 개수만큼 반복 0 1 2 3 4 5 6 7
#     result = []
#     for index in range(3):
#         if i & (1 << index) != 0: # 결과값이 0이 아니라면 index번째 비트는 1이다
#             result.append(arr[index])
#     print(result) # 부분집합


# 5&(1<<0) # 1
# 5&(1<<1) # 0
# 5&(1<<2) # 1
# -> 5를 2진수로 나타내면 101

# 값&(1<<N) != 0 # '값의 N번째 비트가 1이라면'



# 보수
# 어떤 기준 숫자가 되기 위해서 부족한 만큼이 얼만큼인지
# 3의 10의 보수는 7
# 8의 10의 보수는 2

# 1의 보수 - 모든 비트가 1이 되기 위해서 부족한 부분이 무엇인지
# 이진수에서 1의 보수 -> 비트 뒤집기
# 이진수에서 2의 보수 -> 1의 보수(비트 뒤집기)에 1을 더하면 2의 보수

# 음수표현할 때 2의 보수를 사용
# 비트 뒤집고 1을 더했을  때 왼쪽 값이 1이면 음수
# 다시 2의 보수 사용 - 비트 뒤집어서 1을 더하고 나온 양수를 보고 절댓값 알아냄

print(~4)
print(~4+1) # 양수를 음수로
print(~-4+1) # 음수를 양수로

# 실수 - 부동소수점
from decimal import Decimal
a = Decimal('1.2') - Decimal('1.1')
print(a)

a = 1.2 - 1.1
print(a)

a = 1.25
print(f'{a:.1f}')
a = 1.35
print(f'{a:.1f}')
# 파이썬은 반올림을 가까운 짝수 쪽으로 한다.
print(round(4.5)) # 4
print(round(5.5)) # 6


# 1.25를 정확하게 표현하고 싶다면
# 1.25 -> '1.25' -> . 빼기 -> 10으로 나누기 -> 출력할 때 소수점 따로 출력하기
a=1.25
a=str(a)
a=int(a.replace(".",'')) #'125'
a=((a+5)//10)
print(f'{a//10}.{a&10}')
