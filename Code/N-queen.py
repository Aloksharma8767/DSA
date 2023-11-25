chess=[['-' for column in range(4)] for row in range(4)]
for row in chess:
    print(str(row).replace(',','').replace("\'",''))

def check(chess,row,column):
    #to check the column
    for c in range(len(chess)):
        if chess[row][c]=="Q":
            return False
    #to check the row
    for r in range(len(chess)):
        if chess[r][column]=="Q":
            return False
    #To check upper left diagonal
    (row,column)=(i,j)
    while i >= 0 and j >= 0:
        if chess[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
    #To check upper right diagonal
    (row,column)=(i,j)
    while i >= 0 and j < len(chess):
        if chess[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
    #To check lower left diagonal
    (row,column)=(i,j)
    while i >= 0 and j < len(chess):
        if chess[i][j] == 'Q':
            return False
        i = i + 1
        j = j - 1
    #To check lower right diagonal
    (row,column)=(i,j)
    while i >= 0 and j < len(chess):
        if chess[i][j] == 'Q':
            return False
        i = i + 1
        j = j + 1
    
    return True

