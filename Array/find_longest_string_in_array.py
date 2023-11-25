#first and easy way to find it
string = ["apple", "banana", "cherrjinonohy", "date", "fig"]
def check(string):
    print(max(string,key=len))
check(string)
#second and little bit tricky way
def find(string):
    s=[len(i) for i in string]
    b=s.index(max(s))
    print(string[b])
find(string)