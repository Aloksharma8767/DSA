matrix=[[0,1],
        [1,0],
        [1,1],
        [1,0]]
def mark_current_position(matrix,i,j,row,column):
    if (i<=0 or j>=column or j<0 or i>=row or matrix[i][j]!=1):
        return
    #mark current cell as visited
    matrix[i][j]=2
    #Making recursive call in all adjancent direction
    mark_current_position(matrix,i,j+1,row,column)#Right
    mark_current_position(matrix,i,j-1,row,column)#left
    mark_current_position(matrix,i+1,j,row,column)#Top
    mark_current_position(matrix,i-1,j,row,column)#Down
def traverse_matrix(matrix):
    if len(matrix)==0:
        return 0
    row=len(matrix)
    column=len(matrix[0])
    No_of_island=0
    for i in range(row):
        for j in range(column):
            if matrix[i][j]==1:
                mark_current_position(matrix,i,j,row,column)
                No_of_island+=1
    return No_of_island
h=traverse_matrix(matrix)
print(h)