# s = "aaa"
# s = "aaa"
# s="aab"
s="abcd"
def countpalindrome(s):
    result=0
    for i in range(len(s)):
        right=i
        left=i
        # result=0
        while right<len(s) and left>=0 and s[right]==s[left]:
            right+=1
            left-=1
            result=max(result,result+1)
        left=i
        right=i+1
        while left>=0 and right<len(s) and s[right]==s[left]:
            right+=1
            left-=1
            result=max(result,result+1)
    return result
h=countpalindrome(s)
print(h)
#this is written using manachers algorithm in O(n) time complexity
def countSubstrings(s: str) -> int:
    # Preprocess the string to handle even-length palindromes
    processed_str = '#'.join('^{}$'.format(s))

    n = len(processed_str)
    p = [0] * n  # Array to store palindrome lengths

    center, right = 0, 0
    count = 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Attempt to expand palindrome centered at i
        while processed_str[i + p[i] + 1] == processed_str[i - p[i] - 1]:
            p[i] += 1

        # If palindrome expands past right, adjust center and right
        if i + p[i] > right:
            center, right = i, i + p[i]

        # Count the number of palindromic substrings with center at i
        count += (p[i] + 1) // 2

    return count

# Example usage
s = "aaa"
result = countSubstrings(s)
print(result)



