strs= "geeksforgeeks"
def countduplicates(strs):
    dict={}
    for i in range(len(strs)):
        if strs[i] in dict:
            dict[strs[i]]+=1
        else:
             dict[strs[i]]=1
    for key,value in dict.items():
        if value>1:
            print(str(key)+",count=",str(value))
countduplicates(strs)


