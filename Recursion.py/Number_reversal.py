def reve(a):
    if len(str(a))>0:
        return(str(a)[-1]+reve(str(a)[:len(str(a))-1]))
    return ""
a=12345
b=reve(a)
print(b)
#This is another way of writing it
def reverse(s):
    if len(str(s)) == 0:
        return s
    else:
        return reverse(str(s)[1:]) + str(s)[0]
b=reverse(a)
print(b)