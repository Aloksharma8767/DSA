# #it has O(n^2)time complexity 
# def four_sum(arr,x):
#     n=len(arr)
#     two_sum={}
#     for i in range(n):
#         for j in range(1+i,n):
#             two_sum[arr[i]+arr[j]]=[i,j]
#     for i in range(n):
#         for j in range(i+1,n):
#             curr_sum=arr[i]+arr[j]
            
#             if (x-curr_sum) in two_sum:
#                 index=two_sum[x-curr_sum]
#                 if (index[0] != i and index[0] != j and index[1] != i and index[1] != j):
#                     print(arr[i], ", ", arr[j], ", ",
#                           arr[index[0]], ", ", arr[index[1]], sep="")
#                     return
# arr=[10, 2, 3, 4, 5, 9, 7, 8]
# x=23
# four_sum(arr,x)


#it has O(n^2 log n) time complexity
def four_sum_optimized(arr, x):
    n = len(arr)
    arr.sort()  # Sort the array

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if curr_sum == x:
                    print(arr[i], ", ", arr[j], ", ", arr[left], ", ", arr[right], sep="")
                    return
                elif curr_sum < x:
                    left += 1
                else:
                    right -= 1

# Example usage
arr = [10, 2, 3, 4, 5, 9, 7, 8]
x = 23
four_sum_optimized(arr, x)
