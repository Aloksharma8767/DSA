nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
# nums=[0,0]
def proarray(num):
    product=[]
    for i in range(0,len(nums)):
        c=1
        for j in range(0,len(nums)):
            if j==i:
                continue
            else:
                c=c*nums[j]
        product.append(c)
    return product
c=proarray(nums)
print(c)




