#using linear search and its time complexity is O(n)
nums=[1, 2, 8, 10, 10, 12, 19]
def floor_ceiling(nums,x):
    floor=0
    ceil=0
    for i in nums:
        if i>=x:
            ceil=i
            break
        else:
            ceil="ceil doesn't exist in array"
    for i in range(len(nums)-1,-1,-1):
        if nums[i]<=x:
            floor=nums[i]
            break
        else:
            floor="floor doesn't exist in array"
    return floor,ceil
h=floor_ceiling(nums,1)
print(h)
#using binary search and its time complexity is O(log n)
def find_ceil(nums,x):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==x:
            return nums[mid]
        elif x<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    if low>len(nums)-1:
        return "ceil does not exist"
    else:
        return nums[low]
def find_floor(nums,x):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==x:
            return nums[mid]
        elif x<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    if high<0:
        return "floor does not exist"
    else:
        return nums[high]
x=20
h=find_floor(nums,x)
l=find_ceil(nums,x)
print(h,l)




