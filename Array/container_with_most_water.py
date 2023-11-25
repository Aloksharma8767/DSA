height = [1,8,6,2,5,4,8,3,7]
# height =[1,2,1]
# height = [1,1]
# height = [1,2]
# height= [4,3,2,1,4]
def maxarea(height):
    maxe=0
    low=0
    heigh=len(height)-1
    while low<heigh:
        maxe=max(maxe,(min(height[low],height[heigh])*(heigh-low)))
        if height[low]>height[heigh]:
            heigh-=1
        else:
            low+=1
    return maxe
e=maxarea(height)
print(e)



