# 팩토리얼
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

print(f'팩토리얼: {factorial(5)}')

# 리스트 합계
def sum_list(arr):
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1::]) 

numbers = [1,2,3,4,5]
print(f'리스트 합계:{sum_list(numbers)}')

# 피보나치
def pibonachi(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return pibonachi(i-1) + pibonachi(i-2)
    
print(f'피보나치 수:{pibonachi(6)}')


# 제곱
def power1(x, n):
    if n == 0:
        return 1
    return x * power1(x, n-1)

print(f'제곱1: {power1(3, 6)}')

# 제곱 다른 방법으로
def power2(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return power2(x, n // 2) * power2(x, n //2)
    else:
        return x * power2(x, n // 2) * power2(x, n // 2)

print(f'제곱2: {power2(3,6)}')


#최대공약수
def gcd(a, b):
    if b == 0 :
        return a
    # print(a, b)
    
    return gcd(b, a % b)

print(f'최대공약수:{gcd(24, 16)}')