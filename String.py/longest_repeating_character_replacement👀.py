# s ="ABAB"
s = "AABABBA"
def characterReplacement(s,k):
    count={}
    left=0
    length=0
    for right in range(len(s)):
        char=s[right]
        if char not in count:
            count[char]=1
        else:
            count[char]+=1
        length=max(length,right-left+1)
        maxi=length-max(count.values())
        if maxi>k:
            count[s[right]]-=1
            left+=1
    return length
y=characterReplacement(s,1)
print(y)
#Another way
def counter(s,k):
    count={}
    result=0
    left=0
    for right in range(len(s)):
        count[s[right]]=1+count.get(s[right],0)
        while (right-left+1)-max(count.values())>k:
            count[s[left]]-=1
            left+=1
        result=max(result,right-left+1)
    return result
t=counter(s,1)
print(t)

