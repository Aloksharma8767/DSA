from collections import Counter
#it takes O(n) time and O(n) space
def duplicate(arr):
    duplicates=[]
    duplicate={}
    for char in arr:
        duplicate[char]=duplicate.get(char,0)+1
    for char in duplicate:
        if duplicate[char]>1:
            duplicates.append(char)
    if not duplicates:
        return [-1]
    duplicates.sort()
    return duplicates
if __name__=='__main__':
    arr=[2,3,1,2,3]    
    dup=duplicate(arr)
    print(dup)


#we can also do the same thing using counter function form collections module
def duplicate(arr):
    duplicates=[]
    dictonary=Counter(arr) #counter function help us to count the same elements in the list and create dictonary of element and their number of occurance in list in key value pair
    for i in dictonary:
        if dictonary[i]>1:
            duplicates.append(i)
    if not duplicates:
        return [-1]
    duplicates.sort()
    return duplicates
if __name__=='__main__':
    arr=[2,3,1,2,3]    
    dup=duplicate(arr)
    print(dup)


#this code also have O(n) time complexity and O(n) space complixity but it return element in unorderd formate because duplicate element get stored in set
def duplicate(arr):
    arr.sort()
    duplicates=set()
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            duplicates.add(arr[i])
    return -1 if len(duplicates)<=0 else duplicates
if __name__=='__main__':
    arr=[1, 2, 3, 6, 3, 6, 1]
    # arr=[0,3,1]
    j=duplicate(arr)
    print(j)