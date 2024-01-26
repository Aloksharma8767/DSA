#Searching in an array where adjacent differ by at most k
arr = [4, 5, 6, 7, 6]
k = 1
x = 6
def find_index(arr,x,k):
    i=0
    while i<len(arr):
        if arr[i]==x:
            return i
        i=i+max(1,int(abs(arr[i]-x)/k))
    return -1
j=find_index(arr,x,k)
print(j)
#another approch to use index function 
def find_index_of_x(arr,x,k):
    if x in arr:
        return arr.index(x)
    return -1
k=find_index_of_x(arr,x,k)
print (k)

