def counting_sort(input_arr, k):
    """k가 최댓값+1"""
    # counting_arr엔 0부터 k-1개까지 들어가므로 요소가 k개
    counting_arr = [0] * (k)

    # input_arr에 있는 요소 개수를 하나씩 세서 counting_arr에 기록
    for i in input_arr:
        counting_arr[i] += 1

    # counting_arr이 앞의 요소 누적해서 채우기
    for i in range(k-1):
        counting_arr[i+1] += counting_arr[i]

    # input_arr를 순서대로 정렬할 배열 만들기
    Temp_arr = [0] * len(input_arr)

    for i in input_arr[::-1]:
        Temp_arr[counting_arr[i]-1] = i
        counting_arr[i] -= 1
        
    return Temp_arr

    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]


# 오답노트
# reversed() 함수는 원본 데이터를 바꾸지 않고, 순서를 거꾸로 바꾼 이터레이터(반복자) 객체를 반환하는 내장 함수
# 그런데 reversed() 대신 [::-1]로 거꾸로 읽기 가능
# counting_arr에 앞의 요소 누적해서 채우는 거 깜빡했음 - for i in range(k-1): 이 부분에서 영역 설정을 잘못했었음