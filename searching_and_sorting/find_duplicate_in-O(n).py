def duplicate(arr):
    arr.sort()
    list=set()
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            list.add(arr[i])
    return -1 if len(list)<=0 else list
# arr=[1, 2, 3, 6, 3, 6, 1]
arr=[0,3,1]
j=duplicate(arr)
print(j)