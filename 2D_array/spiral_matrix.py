matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
def spiralmatrix(matrix):
    SpiralMatrix=[]
    if not matrix or not matrix[0]:
        return SpiralMatrix
    colbegin=0
    colend=len(matrix[0])-1
    rowbegin=0
    rowend=len(matrix)-1
    while colbegin<=colend and rowbegin<=rowend:
        for i in range(colbegin,colend+1):
            # Traverse Right
            SpiralMatrix.append(matrix[rowbegin][i])
        rowbegin+=1
        for j in range(rowbegin, rowend + 1):
            # Traverse Down
            SpiralMatrix.append(matrix[j][colend])
        colend -= 1
        if rowbegin <= rowend:
            # Traverse Left
            for k in range(colend,colbegin-1,-1):
                SpiralMatrix.append(matrix[rowend][k])
            rowend-=1
        if colbegin <= colend:
                # Traverse Up
                for j in range(rowend, rowbegin - 1, -1):
                    SpiralMatrix.append(matrix[j][colbegin])
                colbegin += 1
    return SpiralMatrix  
u=spiralmatrix(matrix)
print(u)

