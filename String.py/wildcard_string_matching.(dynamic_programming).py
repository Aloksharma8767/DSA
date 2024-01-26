#User function Template for python3

def match(wild, pattern):
    # code here
    if len(wild) == 0 and len(pattern) == 0:
        return True
    if len(wild)>1 and wild[0] == "*":
        i = 0
        while i+1<len(wild) and wild[i+1]=="*":
            i += 1
        wild = wild[i:]
    if len(wild)>1 and wild[0]=="*" and len(pattern)==0:
        return False
    if (len(wild)>1 and wild[0]=="?") or (len(wild) and len(pattern) and wild[0]==pattern[0]):
        return match(wild[1:], pattern[1:])
    if len(wild) and wild[0]=="*":
        return match(wild[1:], pattern) or match(wild, pattern[1:])


if __name__ == '__main__':
    wild = "ge*ks"
    pattern = "geeks"
    h=match(wild,pattern)
    print(h)

#it involve dynaminc problem
