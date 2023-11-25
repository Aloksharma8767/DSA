nums=[7,10,4,3,20,15]
def element(arr,k):
    for i in range(k):
        d=nums.pop((nums.index(min(nums))))
    print(d)
element(nums,3)