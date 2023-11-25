# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5] 
# height = [1,8,6,2,5,4,8,3,7]
height=[7,4,6,8,5,3,9,4]
def trapped_waters(height):
    left_height=[]
    m=height[0]
    for i in range(len(height)):
        if m>=height[i]:
            left_height.append(m)
        else:
            m=height[i]
            left_height.append(height[i])
    right_height=[]
    r=height[-1]
    for i in range(len(height)-1,-1,-1):
        if r>=height[i]:
            right_height.append(r)
        else:
            r=height[i]
            right_height.append(height[i])
    right_height.reverse()
    add=0
    for i in range(len(height)):
        trapped_water=abs(height[i]-min(left_height[i],right_height[i]))
        add+=trapped_water
    return add,left_height
n=trapped_waters(height)
print(n)