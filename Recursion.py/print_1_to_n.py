a=3
# for i in range(a):
#     print(i+1,end=" ")
def num(a):
    if a>0:
        num(a-1)
    print(a,end=" ")
num(a)

