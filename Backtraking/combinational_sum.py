def combinational(arr,target):
    result=[]
    def DEF(index,current,total):
        if total==target:
            result.append(current.copy())
            return
        if index>=len(arr) or total>target:
            return 
        current.append(arr[index])
        DEF(index,current,total+arr[index])
        current.pop()
        DEF(index+1,current,total)
    DEF(0,[],0)
    return result

arr=[2,4,6,8]
target=8
l=combinational(arr,target)
print(l)
