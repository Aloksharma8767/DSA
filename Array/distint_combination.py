def find_all_combinations(arr, k):
  """Finds all the distinct combinations of a given length k with repetition allowed given an integer array.

  Args:
    arr: A list of integers.
    k: The length of the combinations to find.

  Returns:
    A list of all the distinct combinations of length k.
  """
  results = []
  def dfs(current_combination, remaining_elements):
    if len(current_combination) == k:
      results.append(current_combination)
      return
    for element in remaining_elements:
      dfs(current_combination + [element], remaining_elements)
  dfs([], arr)
  return results
# Example usage:
arr = [1, 2, 3]
k = 2
combinations = find_all_combinations(arr, k)
print(combinations)

