#this is brute force approach
txt = "AABAACAADAABAAABAA"
pat = "AABA"
def search(pat, txt):
    len_txt=len(txt)
    len_pat=len(pat)
    for i in range(len_txt-len_pat+1):
        low=0
        while low<len_pat:
            if pat[low]!=txt[i+low]:
                break
            low+=1
        if low==len_pat:
            print("patter found at index:",i)
search(pat,txt)

#below code use rabin-karp algorithm
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    d = 256  # Number of characters in the ASCII set

    # Calculate "pow(d, M-1) % q" to initialize the hash value
    h = pow(d, M-1, q)

    # Calculate the hash value of pattern and the first window of text
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of the current window of text and pattern
        if p == t:
            # Check for characters one by one
            if txt[i:i+M] == pat:
                print("Pattern found at index", i)

        # Calculate hash value for the next window of text: Remove leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get a negative value of t, converting it to positive
            if t < 0:
                t = (t + q)

# Driver code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101  # A prime number
search(pat, txt, q)

def search(pattern, text, prime):
    pattern_length = len(pattern)
    text_length = len(text)
    base = 256  # Number of characters in the ASCII set

    # Calculate "base^(pattern_length-1) % prime" to initialize the hash value
    hash_base = pow(base, pattern_length-1, prime)

    # Calculate the hash value of the pattern and the first window of text
    pattern_hash = sum(ord(pattern[i]) * pow(base, pattern_length-1-i, prime) % prime for i in range(pattern_length)) % prime
    text_hash = sum(ord(text[i]) * pow(base, pattern_length-1-i, prime) % prime for i in range(pattern_length)) % prime

    # Slide the pattern over the text one position at a time
    for i in range(text_length - pattern_length + 1):
        # Check if hash values of the current window of text and pattern match
        if pattern_hash == text_hash:
            # Check for characters one by one
            if text[i:i+pattern_length] == pattern:
                print("Pattern found at index", i)

        # Calculate hash value for the next window of text: Remove leading digit, add trailing digit
        if i < text_length - pattern_length:
            text_hash = (base * (text_hash - ord(text[i]) * hash_base) + ord(text[i + pattern_length])) % prime

            # Ensure the hash value is non-negative
            text_hash = (text_hash + prime) % prime

# Driver code
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
prime = 101  # A prime number
search(pattern, text, prime)

