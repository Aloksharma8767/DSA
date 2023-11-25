# Intervals = [[1,3],[2,4],[6,8],[9,10]]
# Intervals= [[6, 8], [1, 9], [2, 4], [4, 7]]
Intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
def mergeinterval(Intervals):
    Intervals.sort()
    stack=[]
    stack.append(Intervals[0])
    for i in Intervals[1:]:
        if stack[0][0]<=i[0]<=stack[0][1]:
            stack[0][1]=max(i[1],stack[0][1])
        else:
            stack.append(i)
    print(stack)
mergeinterval(Intervals)
