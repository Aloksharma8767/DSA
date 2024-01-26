def findSubArrays(arr, n):
    hashMap = {}
    out = []
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
        if sum1 == 0:
            out.append((0, i))
        al = []
        if sum1 in hashMap:
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return out
if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(arr)
    out = findSubArrays(arr, n)
    print(out)

