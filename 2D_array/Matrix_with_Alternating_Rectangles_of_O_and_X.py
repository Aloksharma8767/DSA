row=int(input("Enter the No of row in matrix:"))
column=int(input("Enter the No of column in matrix:"))
def create_alternating_matrix(row,column):
    matrix=[[None]*column for i in range(row)]
    left=0
    top=0
    Bottom=row
    Right=column
    N="X"
    while left<Right and top<Bottom:
        for i in range(left,Right):
            matrix[top][i]=N
        top+=1
        for i in range(top,Bottom):
            matrix[i][Right-1]=N
        Right-=1
        if top<Bottom:
            for i in range(Right,left-1,-1):
                matrix[Bottom-1][i]=N
            Bottom-=1
        if left<=Right:
            for i in range(Bottom-1,top-1,-1):
                matrix[i][left]=N
            left+=1
        N="O" if N=="X" else "X"  
    for i in range(row):
        for j in range(column):
            print(matrix[i][j],end=" ")
        print()   
c=create_alternating_matrix(row,column) 