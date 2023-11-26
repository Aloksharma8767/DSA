s="babad"
# def longestpalindrome(s):
#     dict={}
#     left=0
#     for i in range(len(s)):
#         for right in range(len(s)):
#             if s[right]==s[left]:
#                 print(s[:right])
#         left+=1
#     # print(s[:right])
# longestpalindrome(s)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s
        
#         Max_Len=1
#         Max_Str=s[0]
#         s = '#' + '#'.join(s) + '#'
#         dp = [0 for _ in range(len(s))]
#         center = 0
#         right = 0
#         for i in range(len(s)):
#             if i < right:
#                 dp[i] = min(right-i, dp[2*center-i])
#             while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
#                 dp[i] += 1
#             if i+dp[i] > right:
#                 center = i
#                 right = i+dp[i]
#             if dp[i] > Max_Len:
#                 Max_Len = dp[i]
#                 Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
#         return Max_Str
def longestPalindrome(s: str) -> str:
    # Base case: if the string is empty or has only one character, it's already a palindrome
    if len(s) <= 1:
        return s
    
    # Initialize variables to keep track of the longest palindrome found
    max_length = 1
    max_substring = s[0]
    
    # Preprocess the string by adding '#' between characters
    s = '#' + '#'.join(s) + '#'
    
    # Initialize an array to store palindrome lengths centered at each index
    palindrome_lengths = [0] * len(s)
    
    # Initialize pointers to keep track of the current palindrome being explored
    center = 0
    right = 0
    
    # Main loop to traverse the modified string
    for i in range(len(s)):
        # If the current index is within the current palindrome, use symmetry
        if i < right:
            palindrome_lengths[i] = min(right - i, palindrome_lengths[2 * center - i])
        
        # Try to expand the palindrome centered at the current index
        while i - palindrome_lengths[i] - 1 >= 0 and i + palindrome_lengths[i] + 1 < len(s) and s[i - palindrome_lengths[i] - 1] == s[i + palindrome_lengths[i] + 1]:
            palindrome_lengths[i] += 1
        
        # If the expanded palindrome reaches beyond the current right boundary, update center and right
        if i + palindrome_lengths[i] > right:
            center = i
            right = i + palindrome_lengths[i]
        
        # Update the longest palindrome information if needed
        if palindrome_lengths[i] > max_length:
            max_length = palindrome_lengths[i]
            # Get the actual substring by removing '#' characters
            max_substring = s[i - max_length:i + max_length + 1].replace('#', '')

    # Return the longest palindromic substring
    return max_substring



