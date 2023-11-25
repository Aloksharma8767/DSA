num=[11,14,15,99]
def findpal(num):
    ans=0
    left=0
    right=len(num)-1
    while left<right:
        if num[left]==num[right]:
            left+=1
            right-=1
        elif num[left]>num[right]:
            right-=1
            num[right]=num[right]+num[right+1]
            ans += 1
        else:
            left+=1
            num[right]=num[left]+num[left-1]
            ans += 1
    print(ans,num)
findpal(num)