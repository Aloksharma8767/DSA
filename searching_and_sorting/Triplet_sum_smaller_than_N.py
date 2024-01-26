"Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. The expected Time Complexity is O(n2)."
arr=[5, 1, 3, 4, 7]
x=12
def counttriplet(arr,x):
    arr.sort()
    ans=0
    for i in range(len(arr)-2):
        left=i+1
        right=len(arr)-1
        while left<right:
            if arr[i]+arr[left]+arr[right]>=x:
                right-=1
            else:
                ans+=(right-left)
                left+=1
    return ans

if __name__=='__main__':
    arr=[5, 1, 3, 4, 7]
    x=12
    j=counttriplet(arr,x)
    print(j)
