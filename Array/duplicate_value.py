# code to find duplicate value in array
arr=[1,2,3]
def duplicate(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return True
    return False
a=duplicate(arr)
print(a)