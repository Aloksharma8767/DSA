class Solution:
    def __init__(self):
        # Initialize the seen flag to False
        self.seen = False

    def mark(self, board, i, j, r, c):
        # Helper function to mark connected regions of 'O' with 'X'
        if i < 0 or i > r - 1 or j < 0 or j > c - 1:
            # If the position is out of bounds, return
            return
        if board[i][j] == 'X':
            # If the position is already marked, return
            return

        # Mark the current position as 'X'
        board[i][j] = 'X'

        # Recursively call mark on neighbors (up, down, left, right)
        self.mark(board, i - 1, j, r, c)
        self.mark(board, i + 1, j, r, c)
        self.mark(board, i, j - 1, r, c)
        self.mark(board, i, j + 1, r, c)

    def dfs(self, board, i, j, r, c, visited):
        # Helper function for depth-first search to identify connected regions
        if i < 0 or i > r - 1 or j < 0 or j > c - 1:
            # If the position is out of bounds, return
            return

        if board[i][j] == 'X' or visited[i][j]:
            # If the position is already marked or visited, return
            return

        if i <= 0 or i >= r - 1 or j <= 0 or j >= c - 1:
            # If the position is on the border, set seen flag to True
            self.seen = True

        # Mark the current position as visited
        visited[i][j] = True

        # Recursively call dfs on neighbors (up, down, left, right)
        self.dfs(board, i - 1, j, r, c, visited)
        self.dfs(board, i + 1, j, r, c, visited)
        self.dfs(board, i, j - 1, r, c, visited)
        self.dfs(board, i, j + 1, r, c, visited)

    def solve(self, board):
        r = len(board)
        if r <= 1:
            # If the number of rows is 0 or 1, no need to process
            return
        c = len(board[0])
        if c <= 1:
            # If the number of columns is 0 or 1, no need to process
            return
        # Initialize a 2D array to keep track of visited positions
        visited = [[False] * c for _ in range(r)]

        # Iterate through the inner region of the board
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    # If 'O' is found and not visited, initiate DFS
                    self.seen = False
                    self.dfs(board, i, j, r, c, visited)
                    if not self.seen:
                        # If the connected region is not on the border, mark it as 'X'
                        self.mark(board, i, j, r, c)
                    self.seen = True


matrix = [["X", "O", "X", "X", "X", "X"],
          ["X", "O", "X", "X", "O", "X"],
          ["X", "X", "X", "O", "O", "X"],
          ["O", "X", "X", "X", "X", "X"],
          ["X", "X", "X", "O", "X", "O"],
          ["O", "O", "X", "O", "O", "O"]]
vi=Solution()
vi.solve(matrix)
print(matrix)
[['X', 'O', 'X', 'X', 'X', 'X'], 
 ['X', 'O', 'X', 'X', 'X', 'X'], 
 ['X', 'X', 'X', 'X', 'X', 'X'], 
 ['O', 'X', 'X', 'X', 'X', 'X'], 
 ['X', 'X', 'X', 'O', 'X', 'O'], 
 ['O', 'O', 'X', 'O', 'O', 'O']]

