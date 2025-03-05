def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr

arr = [9, 5, 1, 4, 3]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)







 # output :
# [1, 3, 4, 5, 9]
