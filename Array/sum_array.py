def find_equal_sum_index(arr):
    total_sum = sum(arr)  # Calculate the total sum of all elements
    left_sum = 0         # Initialize the sum on the left side to 0

    for i in range(len(arr)):
        total_sum -= arr[i]  # Subtract the current element from the total sum

        # Check if the sum on the left side equals the remaining sum on the right side
        if left_sum == total_sum:
            return i  # Found an index that divides the array equally

        left_sum += arr[i]  # Add the current element to the sum on the left side

    return -1  # No such index found

# Example usage:
arr = [1, 2, 3, 4, 5, 5]
index = find_equal_sum_index(arr)
if index != -1:
    print(f"Index {index} divides the array into two subarrays with equal sum.")
else:
    print("There is no such index.")

