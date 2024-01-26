M = [[1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16], 
    [17, 18, 19, 20]] 
for i in range(2*(len(M))-1):
    for j in range(len(M)-1):
        for k in range(len(M)):
            if j+k==i:
                print(M[k][j],end=" ")
    print()
            
#this code have better time complexity than the above code
def print_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for k in range(rows + cols - 1):
        if k < rows:
            row = k
            col = 0
        else:
            row = rows - 1
            col = k - rows + 1

        while row >= 0 and col < cols:
            print(matrix[row][col], end=" ")
            row -= 1
            col += 1

        print()
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix in diagonal order:")
print_diagonal(matrix)
