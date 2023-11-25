s = "anagram"
t = "nagram"
def isanagram(s):
    sorted_s=sorted(s)
    sorted_t=sorted(t)
    return sorted_s==sorted_t
k=isanagram(s)
print(k)
