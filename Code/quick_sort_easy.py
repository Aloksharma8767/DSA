def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    

    sorted_left = quicksort(left)
    sorted_right = quicksort(right)

    return sorted_left + [pivot] + sorted_right
arr = [35, 15, 50, 25, 80, 20, 90, 45]
sorted_arr = quicksort(arr)
print(sorted_arr)
pivot = arr[0]
# left = [x for x in arr[1:] if x < pivot]
# right = [x for x in arr[1:] if x >= pivot]
# print(left)
# print(right)



