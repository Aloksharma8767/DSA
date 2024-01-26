def rotate_image(matrix):
    left,right=0,len(matrix)-1
    while left<right:
        for i in range(right-left):
            top,bottom=left,right
            #save the top left into topleft variable
            topleft=matrix[top][left+i]
            #move the bottom left to top left
            matrix[top][left+i]=matrix[bottom-i][left]
            #move the bottom right to bottom left
            matrix[bottom-i][left]=matrix[bottom][right-i]
            #move the top right to bottom left
            matrix[bottom][right-i]=matrix[top+i][right]
            #move the topleft to top right which is already store in topleft variable
            matrix[top+i][right]=topleft
        right-=1
        left+=1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_image(matrix)
print(matrix)


