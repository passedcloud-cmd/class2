arr = list(range(1, 11))
N = len(arr)

for element in range(1<<N): # 1 x 2^N
    sum = 0
    sub = []
    for i in range(N): # arr 리스트의 모든 요소를 하나씩 검사
        if element&1: # element(2진수)끝자리가 1이면 arr[i]의 스위치가 켜져 있단 뜻
            sum += arr[i]
            # 합이 10 이상이면 중단하고 다음 부분집합으로 넘어가기
            if sum > 10: 
                break # for i
            # 그렇지 않으면 sub 리스트에 arr[i] 추가
            else: sub.append(arr[i])
        # element(2진수)를 오른쪽으로 한칸 이동    
        element >>= 1
    if sum == 10:
        print(' '.join(map(str, sub)))