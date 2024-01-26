def minSwaps(nums):
    n = len(nums)
    temp = [(nums[i], i) for i in range(n)]
    temp.sort()

    visited = [False] * n
    ans = 0

    for i in range(n):
        if visited[i] or temp[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = temp[j][1]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

#Function to find the minimum number of swaps required to sort the array.
def minSwaps(nums):
    new = nums[::]
    new.sort()
    mydict,swaps,N = {},0,len(nums)
    for i in range(N):
        mydict[nums[i]] = i
    
    for i in range(N):
        if nums[i] != new[i]:
            swaps+=1
            temp=nums[i]
            nums[i],nums[mydict[new[i]]]=nums[mydict[new[i]]],nums[i]
            mydict[temp]=mydict[new[i]]
            mydict[new[i]]=i
            
    return swaps
nums = [2, 8, 5, 4]
# nums = [7, 16, 14, 17, 6, 9, 5, 3, 18]
h = minSwaps(nums)
print(h)
