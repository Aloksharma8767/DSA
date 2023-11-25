import time
# nums = [2,3,-2,4]
# nums = [-2,0,-1]
nums=[0,2]
nums=[2,0]
times=[]
def max_arr(nums):
    st=time.time()
    if len(nums)>1:
        arr=[]
        for i in range(len(nums)):
            c=nums[i]
            for j in range(i+1,len(nums)):
                c=c*nums[j]
                arr.append(c)
                arr.append(nums[j])
                arr.append(nums[i])
        print(arr)
        print(max(arr))
    else:
        print(nums[0])
    ed=time.time()
    tt=ed-st
    print(tt)
c=max_arr(nums)
print(c)





