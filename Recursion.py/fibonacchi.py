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
#fibonacchi series using recursive approach
# def fibonacci(a):