strs = ["flower","flow","flight","fight"]
def longestcommonprefix(strs):
    if not strs:
         return ""  
    common_prefix=""
    min_len=min(len(c) for c in strs)
    for i in range(min_len):
        current_char = strs[0][i]
        for string in strs:
            if string[i] != current_char:
                return common_prefix
        common_prefix+=current_char
    return common_prefix
k=longestcommonprefix(strs)
print(k)
