arr=[5,4,3,2,1]
def subarray(arr):
    m=[]
    for i in range(0,len(arr)):
        m.append(i)
        subarray(arr)
# def find_subsets(arr):
#     subsets = [[]]  # Initialize with an empty subset
#     for num in arr:
#         new_subsets = [subset + [num] for subset in subsets]
#         subsets.extend(new_subsets)
#     return subsets

# # Example usage:
# input_array = [1, 2, 3]
# result = find_subsets(input_array)
# for subset in result:
#     print(subset)
subarray(arr)