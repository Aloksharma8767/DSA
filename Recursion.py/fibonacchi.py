#fibonacchi series using iterative approach
def fibo(a):
    prev=0
    temp=1
    if a==1:
        print(prev,end=" ")
    else:
        print(prev,end=" ")
        print(temp,end=" ")
    for i in range(a):
        add=prev+temp
        prev=temp
        temp=add
        print(add,end=" ")
fibo(5)
#fibonacchi using for loop
f=[]
f.append(0)
f.append(1)
for i in range(2,7):
    f.append(f[i-1]+f[i-2])
print(f)
#fibonacchi series using recursive approach
def fibonacchi(num):
    list=[]
    def Calculate(num,first,second):
        if num==0:
            return
        if not list:
            list.append(first)
            list.append(second)
        third=first+second
        list.append(third)
        first=second
        second=third
        Calculate(num-1,first,second)
    Calculate(num,0,1)
    return list

if __name__=='__main__':
    fibo=fibonacchi(5)
    print(fibo)






