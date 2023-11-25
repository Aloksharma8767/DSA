a='ABCDE'
def reve(a):
    if len(a)>0:
        return(a[-1]+reve(a[:len(a)-1]))
    return ""
b=reve(a)
print(b)
#This is another way of writing it
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
b=reverse(a)
print(b)

