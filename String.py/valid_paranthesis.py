# s="()"
s="()[]{}"
def isvalid(s):
    stack=[]
    pairs={
        "(":")",
        "[":"]",
        "{":"}",
    }
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack)==0 or bracket!=pairs[stack.pop()]:
            return False
    return len(stack)==0
o=isvalid(s)
print(o)