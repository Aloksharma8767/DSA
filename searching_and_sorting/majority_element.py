#brut force approach 
def majority_element(nums):
    index=len(nums)//2
    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count+=1
                if count>=index:
                    return i
    return -1
nums=[2,2,1,1,1,9,8]
j=majority_element(nums)
print(j)
# moore's voting algorithm
def majority_vote(nums):
    result,count=0,0
    for n in nums:
        if count==0:
            result=n
        count+=(1 if n==result else -1)
    return result
j=majority_vote(nums)
print(j)

