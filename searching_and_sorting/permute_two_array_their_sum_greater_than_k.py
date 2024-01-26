#Permute two arrays such that sum of every pair is greater or equal to K
def check(a,b,k):
    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i]+b[i]<k:
            return False
    return True
a=[1,2,3,1,2]
b=[1,1,1,1,1]
k=6
h=check(a,b,k)
print(h)

