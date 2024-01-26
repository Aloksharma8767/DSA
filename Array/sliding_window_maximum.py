from collections import deque
# nums = [1,3,-1,-3,5,3,6,7] 
# k = 3
nums=[1]
k=1
arr=[]
right=k-1
left=0
while left<(len(nums)-k+1):
    arr.append(max(nums[left:right+1]))
    right+=1
    left+=1
print(arr)
#Takes sort time 
class Solution:
    def maxSlidingWindow(nums, k):
        mq = deque()
        maxes = []
        
        for i in range(len(nums)):            
            if mq and mq[0] <= i - k: 
                mq.popleft()
            while mq and nums[mq[-1]] <= nums[i]: 
                mq.pop()
            
            mq.append(i)
            if i >= k - 1: 
                maxes.append(nums[mq[0]])
        
        return maxes

#this very less time compare to above two algorithm
class Solution:
    def maxSlidingWindow(nums, k):
        stack = deque()
        for i in range(k):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        curMax = stack[0]
        res = [curMax]
        for i in range(k, len(nums)):
            if nums[i - k] == curMax:
                stack.popleft()
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
            curMax = stack[0]
            res.append(curMax)
        return res
        