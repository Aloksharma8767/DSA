#it has the time complexity of O(n^2)
def minimumcost(nums):
    list=[]
    for i in range(len(nums)):
        cost=0
        for j in range(len(nums)):
            cost+=abs(nums[i]-nums[j])
        list.append(cost)
    print(list)
# nums= [1, 100, 101]
nums=[1, 2, 8, 10, 11, 12, 19,22,30,34]
minimumcost(nums)

#if has the time complexity of O(n)
def minimumcost(nums):
    mid=len(nums)//2
    cost=0
    for i in range(len(nums)):
        cost+=abs(nums[mid]-nums[i])
    print(cost)
nums=[1, 2, 8, 10, 11, 12, 19,22,30,34]
minimumcost(nums)

