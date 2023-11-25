#factorial using iterative approach
a=int(input("Enter the no which factorial you want:"))
def fac(a):
    product=1
    for i in range(a):
        product=product*(i+1)
    print(product)
fac(a)
#factorial using recursive approach
def factorial(a):
    if a<=0:
        return 1
    else:
        return a*factorial(a-1)
b=factorial(a)
print(b)
