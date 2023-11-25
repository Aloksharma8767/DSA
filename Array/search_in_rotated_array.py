def search(arr,no):
    if no in arr:
        print(arr.index(no))
    else:
        print("no is not present in array")
arr=[8,5,7,9,4,3,2,1]
no=int(input("enter the number: "))
search(arr,no)



# def myfun(n):
#     return lambda a:a*n
# m=myfun(2)
# print(m)