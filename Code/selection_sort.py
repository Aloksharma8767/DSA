# n=int(input("enter the size of array: "))
# arr=[]
# for i in range (n):
#     arr.append(int(input("enter the element in array:")))
# print(arr)
# print(len(arr))
# element=int(input("enter the element to be remove: "))
# if element in arr:
#     arr.remove(element)
# else:
#     print("you entered element is not present in array")
# print(arr)
arr=[35,15,50,25,80,20,90,45,99,88,77,11]
def select(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
select(arr)
#This is selection sort using min function to find minimum element in array
a=[10,9,8,7,6,5,4,3,2,1]
def selection(a):
    for i in range(len(a)):
        b=a.index(min(a[i::]))
        if a[i]>a[b]:
            a[i],a[b]=a[b],a[i]
        # print(a)
    print(a)
selection(a)
