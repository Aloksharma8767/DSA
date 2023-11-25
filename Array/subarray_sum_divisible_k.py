nums=[2,7,6,1,4,5]
# nums=[-2, 2, -5, 12, -11, -1, 7]
# nums=[1,2,-2,2,2]
def SumDivByK(nums,k):
    count=0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum%k==0:
                count=max(count,j-i+1)
    print(count)
SumDivByK(nums,2)