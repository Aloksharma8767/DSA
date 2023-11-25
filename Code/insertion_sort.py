a=[35,15,50,25,80,20,90,45,99,66]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if i>0:
        for k in range(i):
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
                i=i-1
    # print(a)
print(a)
# insertion sort can be done using this code also
a=[8,9,7,6,5,4]
for i in range(1,len(a)):
    key=a[i] # 7
    j=i-1 # 2-1 =1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j=j-1
        print(a)
    a[j+1]=key
    # print(a)
print(a)


