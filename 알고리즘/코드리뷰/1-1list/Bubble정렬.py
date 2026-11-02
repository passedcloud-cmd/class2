def bubble_sort(arr):
    N = len(arr)
    # 두 개씩 비교하니까 N-1번까지 진행
    for i in range(N-1):
		    # i번 진행할 때마다 맨 뒤에 숫자가 고정되니까 N-1-i번까지 진행
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)

numbers2 = [6, 456, 54, 22, 3213, 9887]
sorted_numbers = bubble_sort(numbers2)
print("정렬 후:", sorted_numbers)
