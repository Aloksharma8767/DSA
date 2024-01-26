def count_sort(nums):
    maximum=max(nums)+1
    count_of_element=[0]*maximum
    Result=[0]*len(nums)
    for i in range(len(nums)):
        count_of_element[nums[i]]+=1
    for i in range(1,len(count_of_element)):
        count_of_element[i]+=count_of_element[i-1]
    I=len(nums)-1
    while I>=0:
        Result[count_of_element[nums[I]]-1]=nums[I]
        count_of_element[nums[I]]-=1
        I-=1
    return Result
nums=list(map(int,input().split()))
h=count_sort(nums)
print(h)
