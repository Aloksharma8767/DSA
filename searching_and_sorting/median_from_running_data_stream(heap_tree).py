arr=[5, 15, 1, 3]
def medianfind(nums):
    if len(nums)==1:
        return nums[0]
    remainder=len(nums)%2
    qotient=len(nums)//2
    if remainder != 0:
        return nums[qotient]
    else:
        med=(nums[qotient]+nums[qotient-1])//2
        return med  
def inserting(arr):
    arr_len=len(arr)
    nums=[]
    median=[]
    for i in range(arr_len):
        j=i
        while j>0 and arr[i]<nums[j-1]:
            j-=1
        nums.insert(j,arr[i])
        median.append(medianfind(nums))        
    return median
call=inserting(arr)
print(call)
