#### 진수

binary_str = '0110'
num = int(binary_str, 2) # 10진수로 만들기
print(num) # 6

num =250
format(num, 'X') # 16진수로 만들기 # 'FA'
hex(num)[2:].upper() # 16진수로 만들기. # 'FA'

format(6, '04b') #'0110'

bin(6) # '0b110'
# print(type(bin(6))) # str
bin(6).replace('0b','') # '110'

#16진수를 2진수로 바꾸기
her_str = "4A"
result = ''
for ch in her_str:
    num = int(ch, 16) #10진수로
    result += format(num, '04b') # 2진수로
print(result) # 01001010

# 8진수를 2진수로 바꾸기
oc_str = '75'
result = ''
for ch in oc_str:
    num = int(ch, 8)
    result += format(num, '03b')
print(result) # 111101
print(int(result,2)) # 61

