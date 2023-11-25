num=[1,2,3,5,3]
# n=1
# while n<len(num):
#     if n in num:
#         n+=1
#     else:
#         print(n)
#         break
# for i in range(0,len(num)-1):
#     for j in range(i+1,len(num)):
#         if num[i]==num[j]:
#             print(num[i])
def findDuplicateAndMissing(nums):
    n = len(num) #5
    S1 = sum(x * x for x in nums) #48
    S2 = sum(nums) #14
    
    S2_expected = n * (n + 1) // 2  #15
    S1_expected = sum(x * x for x in range(1, n + 1)) #55
    
    delta_S = S2_expected - S2
    delta_Sq = S1_expected - S1
    
    A = (delta_S + delta_Sq) // 2
    B = A - delta_S
    
    return A, B
k=findDuplicateAndMissing(num)
print(k)
# S1 = sum(x * x for x in num)
# print(S1)
# S2=sum(num)
# print(S2)
# S1_expected = sum(x * x for x in range(1, n + 1))
# print(S1_expected)
# S2_expected = n * (n + 1) // 2
# print(S2_expected)


