def merging_array(arr1,arr2,n,m):
    for i in range(m):
        arr1.append(arr2[i])
    arr1.sort()
    del arr2[:]
    for j in range(n,n+m):
        arr2.append(arr1[j])
    del arr1[n:n+m+1]

if __name__=='__main__':
    arr1 = [1, 3, 5, 7]
    arr2 =[0, 2, 6, 8, 9]
    n=len(arr1)
    m=len(arr2)
    merging_array(arr1,arr2,n,m)
    print(arr1)
    print(arr2)
# using del method and list slicing  we can delete elements in list 