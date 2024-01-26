matrix=[
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
def issafe(i,j,visited,matrix,n):
    if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or matrix[i][j] == 0:
        return False
    return True

def rat_maze(matrix,visited,i,j,n,path,paths):
    if i == n-1 and j == n-1:
        paths.append(path)
        return 
    
    visited[i][j]=True
    # down  
    if issafe(i+1,j,visited,matrix,n):
        rat_maze(matrix,visited,i+1,j,n,path+"D",paths)   
    # left
    if issafe(i,j-1,visited,matrix,n):
        rat_maze(matrix,visited,i,j-1,n,path+"L",paths)
    # up
    if issafe(i-1,j,visited,matrix,n):
        rat_maze(matrix,visited,i-1,j,n,path+"U",paths)
    # right
    if issafe(i,j+1,visited,matrix,n):
        rat_maze(matrix,visited,i,j+1,n,path+"R",paths)
    visited[i][j]=False

if __name__=='__main__':
    n=len(matrix)
    paths=[]
    visited=[[False]*n for _ in range(n)]
    rat_maze(matrix,visited,0,0,n,"",paths)
    print(paths)
