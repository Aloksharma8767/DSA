# nums = [-1,0,1,2,-1,-4]
nums=[-2,0,1,1,2]
def threesum(nums):
    result=[]
    nums.sort()
    if len(nums)<3:
        return result
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break  
        if i > 0 and nums[i] == nums[i - 1]:
            continue     
        low,high=i+1,len(nums)-1
        while low<high:
            crr=nums[i]+nums[low]+nums[high]
            if crr>0:
                high -=1
            elif crr<0:
                low +=1
            else:
                result.append([nums[i],nums[low],nums[high]])
                low +=1
                high-=1
                while low<high and nums[low]== nums[low-1]:
                    low +=1
                while low<high and nums[high]==nums[high+1] :
                    high-=1
    return result
d=threesum(nums)
print(d)
