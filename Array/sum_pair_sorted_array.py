num=[11, 15, 6, 8, 9, 10]
def pair(num,x):
    for i in range(len(num)):
        for j in range(1,len(num)):
            if num[i]+num[j]==x:
                return True
    return False
d=pair(num,16)
print(d)
#this is two pointer solution and it take O(n) time less than above code
def spar(num,x):
    num.sort()
    left=0
    right=len(num)-1
    while left<right:
        if num[left]+num[right]>x:
            right-=1
        elif num[left]+num[right]<x:
            left+=1
        else:
            return True
    return False
d=spar(num,16)
print(d)