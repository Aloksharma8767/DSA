nums = [3,2,3,1,2,4,5,5,6]
def element(arr,k):
    for i in range(k):
        d=nums.index(max(nums))
        c=nums.pop(d)
    print(c)
element(nums,4)



