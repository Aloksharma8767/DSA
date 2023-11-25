def maxsubarry(arr):
    mi=[]
    for i in range(0,len(arr)-1):
        ma=[]
        add=arr[i]
        for j in range(i+1,len(arr)-1):
            add=add+arr[j]
            ma.append(add) 
        if ma!=[]:
            mi.append(max(ma))
    return f"The maximum sum of subarray is {max(mi)}"
arr=[-2,1,-3,4,-1,2,1,-5,4]
a=maxsubarry(arr)
print(a)

