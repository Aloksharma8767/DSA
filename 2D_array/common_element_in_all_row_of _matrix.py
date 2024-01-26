matrix=[[1, 2, 3, 4,22, 5,6],
        [2, 4,22, 5, 8, 10,6],
        [3, 5, 7, 9,22, 11,6],
        [1,22, 3, 5, 7, 9,6]]
def count(matrix,num):
    counter=0
    for R in matrix:
        if num in R:
            counter+=1
    return counter
def traverse_matrix(matrix):
    if len(matrix)==0:
        return 
    numbers=[]
    row=len(matrix)
    column=len(matrix[0])
    for j in range(column):
        num=matrix[0][j]
        c=count(matrix,num)
        if c==4:
            numbers.append(matrix[0][j])
    return numbers if len(numbers)>=0 else -1
h=traverse_matrix(matrix)
print(h)

#second approach 
def common_elements(matrix, rows, columns):
    # Map
    hashmap = {}

    for i in range(columns):
        hashmap[matrix[0][i]] = 1

    for i in range(1, rows):
        for j in range(columns):
            # Store and avoid duplicate elements of the same row
            if matrix[i][j] in hashmap and hashmap[matrix[i][j]] == i:
                hashmap[matrix[i][j]] += 1

            if i == rows - 1 and matrix[i][j] in hashmap and hashmap[matrix[i][j]] == rows:
                print(matrix[i][j], end=" ")

# Input
mat = [
    [1, 2, 1, 4, 8],
    [8, 7, 8, 5, 1],
    [8, 7, 7, 3, 1],
    [8, 1, 2, 7, 9]
]
# Function call
common_elements(mat, len(mat), len(mat[0]))




