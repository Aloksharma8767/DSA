# # m=[8,6,4,7,5]
# m=[3,2,1]
# for i in range(len(m)-1,0,-1):
#     if m[i-1]<m[i]:
#         break
# for j in range(len(m)-1,0,-1):
#     if m[j]>m[i-1]:
#         m[j],m[i-1]=m[i-1],m[j] 
#         break
#     else:
#         for i in range(1,len(m)):
#             key=m[i] # 7
#             j=i-1 # 2-1 =1
#             while j>=0 and key<m[j]:
#                 m[j+1]=m[j]
#                 j=j-1
#             m[j+1]=key
# print(m)
# def three_sum(nums):
#     # Sort the array to easily handle duplicates and for the three-pointer approach
#     nums.sort()
#     result = []
#     for i in range(len(nums) - 2):
#         # Skip duplicates for the first element
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             curr_sum = nums[i] + nums[left] + nums[right]
#             if curr_sum == 0:
#                 result.append([nums[i], nums[left], nums[right]])
#                 # Skip duplicates for the second element
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 # Skip duplicates for the third element
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#             elif curr_sum < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return result

# # # Example usage:
# nums = [-1, 0, 1, 2, -1, -4]
# result = three_sum(nums)
# print(result)
#ojllm
# def threeSum(nums):
#     nums.sort()
#     answer = []    
#     if len(nums) < 3:
#         return answer    
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             break        
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue        
#         low, high = i + 1, len(nums) - 1
#         while low < high:
#             s = nums[i] + nums[low] + nums[high]
#             if s > 0:
#                 high -= 1
#             elif s < 0:
#                 low += 1
#             else:
#                 answer.append([nums[i], nums[low], nums[high]])
#                 lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]
                
#                 while low < high and nums[low] == lastLowOccurrence:
#                     low += 1
                
#                 while low < high and nums[high] == lastHighOccurrence:
#                     high -= 1
#     return answer
# p=threeSum(nums)
# print(p)
# l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
# for ele in enumerate(l1):
# 	print (ele)

# changing index and printing separately
# for count, ele in enumerate(l1):
# 	if count>0:
# 		continue
# 	print (count, ele)

# getting desired output from tuple
# for count, ele in enumerate(l1):
# 	print(count)
# 	print(ele)
def merge_intervals(intervals):
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the merged list is empty or if the current interval does not overlap with the previous one
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # If the current interval overlaps with the previous one, merge them
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

# Example usage:
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
# result = merge_intervals(intervals)
# print(result)
