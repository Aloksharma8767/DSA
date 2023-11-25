a=[9,8,7,6,5,4,3,2,1]
for j in range(len(a)):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    print(a)
print(a)