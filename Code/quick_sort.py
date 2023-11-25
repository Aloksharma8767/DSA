def quicksort(arr,first,last):
    a=arr[first]
    b=first+1
    c=last
    while True:
        while b<=c and arr[b]<=a:
            b+=1
        while b<=c and arr[c]>=a:
            c-=1
        if c<b:
            break
        else:
            arr[b],arr[c] = arr[c],arr[b]
    arr[first],arr[c] = arr[c],arr[first]
    return c
def quick(arr,first,last):
    if first<last:
        p=quicksort(arr,first,last)
        quick(arr,first,p-1)
        quick(arr,p+1,last)
arr=[35,15,50,25,80,20,90,45,99,88,77,11]
n=len(arr)
quick(arr,0,n-1)
print(arr)
