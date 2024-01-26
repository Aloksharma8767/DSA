#manachers algorithm
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
########################################
def longest_palindromic_substring(s):
    # Preprocess the string to insert special characters
    # to handle even-length palindromes
    processed_str = '#'.join('^{}$'.format(s))

    n = len(processed_str)
    p = [0] * n
    center, right = 0, 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Attempt to expand palindrome centered at i
        while processed_str[i + 1 + p[i]] == processed_str[i - 1 - p[i]]:
            p[i] += 1

        # If palindrome centered at i expands past right,
        # adjust center and right boundary
        if i + p[i] > right:
            center, right = i, i + p[i]

    # Find the maximum element in p
    max_len, center_index = max((n, i) for i, n in enumerate(p))

    # Extract the palindrome substring and remove special characters
    start = (center_index - max_len) // 2
    end = start + max_len

    return s[start:end]

# Example usage
s = "babad"
result = longest_palindromic_substring(s)
print(result)





