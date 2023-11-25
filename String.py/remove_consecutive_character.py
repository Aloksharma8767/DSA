# s="aabb"
s="aabaa"
def removeConsecutiveCharacter(s):
    duplicate=[]
    duplicate.append(s[0])
    count=0
    for i in range(1,len(s)):
        if s[i]==duplicate[count]:
            continue
        else:
            duplicate.append(s[i])
            count+=1
    str="".join(duplicate)
    return str
r=removeConsecutiveCharacter(s)
print(r)

