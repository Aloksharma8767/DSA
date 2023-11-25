def next_permutation(nums):
    # Find the first element from the right that is smaller than the element next to it
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the smallest element to the right of i and greater than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray to the right of i
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage:
nums = [5,6,4,7,3]
next_permutation(nums)
print(nums) 

#Another code for finding next permutation 
# m=[8,6,4,7,5]
m=[3,2,1]
for i in range(len(m)-1,0,-1):
    if m[i-1]<m[i]:
        break
for j in range(len(m)-1,0,-1):
    if m[j]>m[i-1]:
        m[j],m[i-1]=m[i-1],m[j] 
        break
    else:
        for i in range(1,len(m)):
            key=m[i] # 7
            j=i-1 # 2-1 =1
            while j>=0 and key<m[j]:
                m[j+1]=m[j]
                j=j-1
            m[j+1]=key
print(m)

