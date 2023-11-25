from itertools import combinations
def generate_combinations(arr, r):
    # Use itertools.combinations to generate all combinations of r elements
    result = list(combinations(arr, r))
    # Print the generated combinations
    for combination in result:
        print(combination)
# Example usage:
arr = [1, 2, 3, 4]
r = 3
generate_combinations(arr, r)
#without using itertool
def generate_combinations(arr, r, current=[], start=0):
    if len(current) == r:
        print(tuple(current))
        return

    for i in range(start, len(arr)):
        # Choose the current element
        current.append(arr[i])

        # Recursively generate combinations for the remaining elements
        generate_combinations(arr, r, current, i + 1)

        # Backtrack: remove the last element to try the next one in the next iteration
        current.pop()

# Example usage:
arr = [1, 2, 3, 4]
r = 2
generate_combinations(arr, r)

