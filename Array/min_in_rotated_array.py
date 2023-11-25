# from datetime import datetime
from time import time
num=[8,9,7,5,0]
def findmin(num):
    num.sort()
    return min(num)
if __name__ == '__main__':
    init=time()
    s=findmin(num)
    print(s,time()-init)