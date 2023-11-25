def reverse(arr):
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
arr=[9,8,7,6,5,4,3,2,1,-1,-2,-3,11,22,333,44,55,66,77,88,99]
a=reverse(arr)
print(a)

