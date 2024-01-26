# #using linear search
# def allocat_pages(arr,pages):
#     student=1
#     No_of_pages=0
#     for i in range(len(arr)):
#         if No_of_pages+arr[i]<=pages:
#             No_of_pages+=arr[i]
#         else:
#             student+=1
#             No_of_pages=arr[i]
#     return student
# def book_allocation(arr,m):
#    low=max(arr)
#    high=sum(arr)
#     for page in range(low,high):
#         No_of_student=allocat_pages(arr,page)
#         if No_of_student==m:
#             return page

# if __name__=='__main__':
#     arr=[12,34,67,90]
#     h=book_allocation(arr,2)
#     print(h)


#using binary search
def allocat_pages(arr,pages):
    student=1
    No_of_pages=0
    for i in range(len(arr)):
        if No_of_pages+arr[i]<=pages:
            No_of_pages+=arr[i]
        else:
            student+=1
            No_of_pages=arr[i]
    return student
def book_allocation(arr,m):
    low=max(arr)
    high=sum(arr)
    while (low<=high):
        mid=(low+high)//2
        No_of_student=allocat_pages(arr,mid)
        if No_of_student>m:
            low=mid+1
        else:
            high=mid-1
    return low
    
if __name__=='__main__':
    arr=[12,34,67,90]
    h=book_allocation(arr,2)
    print(h)
