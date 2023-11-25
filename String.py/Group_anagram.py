strs = ["eat","tea","tan","ate","nat","bat"]
def groupanagaram(strs):
    anagram={}
    for string in strs:
        sorted_string="".join(sorted(string))
        if sorted_string not in anagram:
            anagram[sorted_string]=[]
        anagram[sorted_string].append(string)
    return list(anagram.values())
t=groupanagaram(strs)
print(t)

