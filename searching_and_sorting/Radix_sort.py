def Countsort(num,p):
    n=len(num)
    Res=[0]*n
    C=[0]*10
    for i in range(0,n):
        temp=num[i]//p
        C[temp%10]+=1
    for i in range(1,10):
        C[i]=C[i]+C[i-1]
    i=n-1
    while i>=0:
        temp=num[i]//p
        Res[C[temp%10]-1]=num[i]
        C[temp%10]-=1
        i=i-1
    for i in range(0,n):
        num[i]=Res[i]
def Radixsort(num):
    maximum=max(num)
    n=1
    while maximum//n>0:
        Countsort(num,n)
        n=n*10
num=list(map(int,input().split()))
Radixsort(num)
print(num)