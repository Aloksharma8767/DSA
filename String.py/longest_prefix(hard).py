#knuth-morris-pratt string algorithm
s="acccbaaacccbaacd"
def longest_prefix_suffix(s):
    lps=[0]*len(s)
    left=0
    right=1
    while right<len(s):
        if s[right]==s[left]:
            left+=1
            lps[right]=left
            right+=1
        else:
            if left==0:
                lps[right]=0
                right+=1
            else:
                left=lps[left-1]
    return lps[-1] if lps[-1]!=0 else 0
j=longest_prefix_suffix(s)
print(j)



