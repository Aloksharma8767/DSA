def next_permutation(nums):
    # Find the first element from the right that is smaller than the element next to it
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    print(i)

    if i >= 0:
        # Find the smallest element to the right of i and greater than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        print(nums[i])
        print(nums[j])

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray to the right of i
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage:
nums = [1, 2, 3, 6, 5, 4]
next_permutation(nums)
print(nums) 


