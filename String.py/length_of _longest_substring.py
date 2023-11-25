strs="abcabcbb"
# strs = "bbbbb"
# strs = "pwwkew"
def lengthOfLongestSubstring(strs):
    substring=[]
    length=[]
    for i in range(len(strs)):
        sub_string=strs[i]
        for j in range(i+1,len(strs)):
            if strs[j] in sub_string:
                break
            else:
                sub_string+=strs[j]
        if len(sub_string) not in length:
            length.append(len(sub_string))
            # substring.append(str(sub_string))
    print(substring[length.index(max(length))])
lengthOfLongestSubstring(strs)
# two pointer technique 
# strs="abcabcbb"
strs = "bbbbb"
def lengthOfLongestSubstring(s):
    dict={}
    left=0
    length=0
    for right in range(len(s)):
        if s[right] in dict and dict[s[right]]>=1:
            left=dict[s[right]]+1
        else:
            length=max(length,right-left+1)
        dict[s[right]]=right
    return length
u=lengthOfLongestSubstring(strs)
print(u)
