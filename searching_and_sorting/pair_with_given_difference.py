arr=[2,3,5,20,50,80]
n=78
for i in range(len(arr)-1,-1,-1):
    if arr[i]>n:
        differ=arr[i]-n
        if differ in arr:
            k=arr.index(differ)
            print(f"Pair found:({arr[k]},{arr[i]})")
            break
def find_pair(nums,n):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                continue
            if arr[i]-arr[j]==n:
                return(f"Pair found:({arr[i]},{arr[j]})")
    return ("pair not found")

                
