def count_inversion(arr):
    # count=0
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        count_inversion(L)
        count_inversion(R)
        i=j=k=0
        count=0
        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                arr[k]=L[i]
                i+=1
                k+=1
            else:
                arr[k]=R[j]
                k+=1
                j+=1
            #here there is inversion because of a[i]>a[j] therefor we subtracted the i form array of L
                count+=len(L)-i
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        return count
arr=[2, 4, 1, 3, 5 ]
h=count_inversion(arr)
print(h)
print(arr)

