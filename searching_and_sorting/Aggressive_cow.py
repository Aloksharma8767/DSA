#using linear search
def can_we_place(arr,dis,cow):
    first_cow=arr[0]
    cow_count=1
    for i in range(1,len(arr)):
        if arr[i]-first_cow>=dis:
            cow_count+=1
            first_cow=arr[i]
        if cow_count>=cow:
            return True
    return False
def aggressive_cow(arr,k):
    min_dist_cow=0
    arr.sort()
    min_dist=1
    max_dist=max(arr)-min(arr)
    for i in range(min_dist,max_dist+1):
        if can_we_place(arr,i,k):
            min_dist_cow=max(min_dist_cow,i)
    return min_dist_cow

if __name__=='__main__':
    arr=[10, 1, 2, 7, 5]
    arr=[1,2,3,4,6]
    h=aggressive_cow(arr,3)
    print(h)

#using binary search
def can_we_place(arr,dis,cow):
    first_cow=arr[0]
    cow_count=1
    for i in range(1,len(arr)):
        if arr[i]-first_cow>=dis:
            cow_count+=1
            first_cow=arr[i]
        if cow_count>=cow:
            return True
    return False
def aggressive_cow(arr,k):
    arr.sort()
    ans=0
    min_dist=1
    max_dist=arr[len(arr)-1]-arr[0]
    while min_dist<=max_dist:
        mid=(max_dist+min_dist)//2
        if can_we_place(arr,mid,k):
            ans=max(ans,mid)
            min_dist=mid+1
        else:
            max_dist=mid-1
    return ans
if __name__=='__main__':
    arr=[1, 2, 4, 8, 9]
    h=aggressive_cow(arr,3)
    print(h)


