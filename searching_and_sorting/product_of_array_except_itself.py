def productExceptSelf(nums):
    n=len(nums)
    result=[1]*n
    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]
    postfix=1
    for i in range(n-1,-1,-1):
        result[i]=postfix*result[i]
        postfix*=nums[i]
    print(result)
nums = [10, 3, 5, 6, 2]
productExceptSelf(nums)

#another way of writing this code
def productExceptSelf(nums):
    n = len(nums)

    # Initialize output arrays
    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n

    # Calculate prefix products
    left_product[0] = 1
    for i in range(1, n):
        left_product[i] = left_product[i-1] * nums[i-1]

    # Calculate suffix products
    right_product[n-1] = 1
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * nums[i+1]

    # Calculate the final result
    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result
# Example usage:
nums = [10, 3, 5, 6, 2]
result = productExceptSelf(nums)
print(result)
