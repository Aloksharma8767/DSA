import string
s = "A man, a plan, a canal: Panama"
def isPalindrome(s):
    for punctuation in string.punctuation:
        s = (s.lower().replace(punctuation, '').replace(' ',''))
    l=s[::-1]
    if l==s or s==" ":
        print(True)
    else:
        print(False)
isPalindrome(s)
#This is another approch to solve it
s = "A man, a plan, a canal: Panama"
def isPalindrome(s):
    s = s.lower().replace(" ","").translate(str.maketrans('', '', string.punctuation))
    l=s[::-1]
    if l==s or s==" ":
        print(True)
    else:
        print(False)
isPalindrome(s)






