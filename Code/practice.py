# def nextPermutation(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     # Base case
#     if nums == sorted(nums, key=lambda x: -x):
#         nums.sort()
#         return
#     for i in range(n - 1, 0, -1):
#         if nums[i - 1] < nums[i]:
#             # Find the first value that is less than the current value
#             min_idx, min_val = n, float('inf')
#             for j in range(n - 1, i - 1, -1):
#                 if nums[j] > nums[i - 1] and nums[j] < min_val:
#                     min_val = nums[j]
#                     min_idx = j
#             nums[i - 1], nums[min_idx] = nums[min_idx], nums[i - 1]
#             # Bubble Sort
#             while True:
#                 swapped = False
#                 for k in range(i, n - 1):
#                     if nums[k] > nums[k + 1]:
#                         swapped = True
#                         nums[k], nums[k + 1] = nums[k + 1], nums[k]
#                 if swapped == False: break
                
#             return
# l=[1,2,3,4,5,6,7]
# print(nextPermutation(l))

# for i in range(len(p)-1):
#     x_m=(x_m*x)%q
#     print(x_m)
# print(x_m)
# from collections import defaultdict
# graph = defaultdict(list)
# v,e=map(int,input().split())
# for i in range(e):
#     u,v=map(str,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# for v in graph:
#     print(v,graph[v])
# print(graph)

# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# Name=input()
# if Name in contacts:
#     print(contacts[Name])
# contacts.append( ('tiger', 1))
# print(contacts)
# col=[4]*4
# print(col)
# board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# def cha(board):
#     left = 0
#     right = len(board[0])
#     top = 0
#     bottom = len(board)
#     r="X"
#     while left<right and top<bottom:  
#         for i in range(left, right):
#             board[top][i] = r  # right
#         top += 1
#         for i in range(top, bottom ):
#             board[i][right-1] = r  # down
#         right -= 1
#         if top <= bottom:
#             for i in range(right-1, left - 1, -1):
#                 board[bottom-1][i] = r  # left
#             bottom -= 1
#         if left <= right:
#             for i in range(bottom-1, top - 1, -1):
#                 board[i][left] = r  # up
#             left += 1
#         r = "O" if r == "X" else "X"
# cha(board)
# for i in range(len(board)):
#         for j in range(len(board[0])):
#             print(board[i][j], end = " ")
#         print()
# def create_alternating_matrix(m, n):
#     # Initialize the matrix with 'X' for all elements
#     matrix = [['X' for _ in range(n)] for _ in range(m)]

#     # Loop over the rectangles to alternate 'X' and '0'
#     for i in range(1, min(m, n) // 2 + 1):
#         # Set '0' in the top and bottom rows of the current rectangle
#         for j in range(i, n - i):
#             matrix[i][j] = '0'
#             matrix[m - 1 - i][j] = '0'

#         # Set '0' in the left and right columns of the current rectangle
#         for j in range(i, m - i):
#             matrix[j][i] = '0'
#             matrix[j][n - 1 - i] = '0'

#     # Return the resulting matrix
#     return matrix

# # Input: Ask the user for the number of rows and columns
# m = int(input("Enter the number of rows (m): "))
# n = int(input("Enter the number of columns (n): "))

# # Create and print the alternating matrix
# result_matrix = create_alternating_matrix(m, n)
# for row in result_matrix:
#     print(" ".join(row))
# for i in range(5):
#     print(i,end="")
# print()
# for i in range(1,2):

#     print(i,end="")
# def productExceptSelf(nums, n):
#     left = [1] * n
#     right = [1] * n
#     result = [1] * n
#     left[0] = 1
#     for i in range(1, n):
#         left[i] = left[i-1] * nums[i-1]
#     right[n-1] = 1
#     for j in range(n-2, -1, -1):
#         right[j] = right[j+1] * nums[j+1]
#     for i in range(n):
#         result[i] = left[i] * right[i]
#     return result
# nums=[10, 3, 5, 6, 2]
# n=len(nums)
# u=productExceptSelf(nums,n)
# print(u)


# def productExceptSelf(nums):
#     n = len(nums)

#     # Initialize output arrays
#     left_product = [1] * n
#     right_product = [1] * n
#     result = [1] * n

#     # Calculate prefix products
#     left_product[0] = 1
#     for i in range(1, n):
#         left_product[i] = left_product[i-1] * nums[i-1]

#     # Calculate suffix products
#     right_product[n-1] = 1
#     for i in range(n-2, -1, -1):
#         right_product[i] = right_product[i+1] * nums[i+1]

#     # Calculate the final result
#     for i in range(n):
#         result[i] = left_product[i] * right_product[i]

#     return result

# # Example usage:
# nums = [10, 3, 5, 6, 2]
# result = productExceptSelf(nums)
# print(result)
# for i in range(1,4):
#     print(i)
# column=4
# visited=[[False]*column for _ in range(4)]
# print(visited)

# def is_valid_move(matrix, x, y, visited):
#     n = len(matrix)
#     return 0 <= x < n and 0 <= y < n and matrix[x][y] == 1 and not visited[x][y]

# def find_paths(matrix):
#     def dfs(x, y, path, visited):
#         nonlocal paths

#         if x == n - 1 and y == n - 1:
#             paths.append(path)
#             return

#         visited[x][y] = True

#         for dx, dy, direction in directions:
#             new_x, new_y = x + dx, y + dy
#             if is_valid_move(matrix, new_x, new_y, visited):
#                 dfs(new_x, new_y, path + direction, visited)

#         visited[x][y] = False

#     n = len(matrix)
#     paths = []
#     visited = [[False] * n for _ in range(n)]
#     directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]

#     if matrix[0][0] == 1:
#         dfs(0, 0, "", visited)

#     return sorted(paths)

# # Example usage:
# matrix = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [0, 1, 0, 0],
#     [1, 1, 1, 1]
# ]

# result = find_paths(matrix)
# print(result)

# def hello(j):
#     k=j
# print(hello("m"))

# matrix = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 1]
# ]

# def issafe(i, j, visited, matrix, n):
#     return 0 <= i < n and 0 <= j < n and not visited[i][j] and matrix[i][j] == 1

# def rat_maze(matrix, n):
#     paths = []
#     visited = [[False] * n for _ in range(n)]
#     stack = [(0, 0, "", visited)]

#     directions = [(1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R')]

#     while stack:
#         i, j, path, current_visited = stack.pop()

#         if i == n - 1 and j == n - 1:
#             paths.append(path)

#         current_visited[i][j] = True

#         # Explore all possible directions using a loop
#         for dx, dy, direction in directions:
#             new_i, new_j = i + dx, j + dy
#             if issafe(new_i, new_j, current_visited, matrix, n):
#                 stack.append((new_i, new_j, path + direction, [row[:] for row in current_visited]))

#     return paths

# if __name__ == '__main__':
#     n = len(matrix)
#     result = rat_maze(matrix, n)
#     print(result)

# def fact(num):
#     if num==1:
#         return num
#     fac=(num * fact(num-1))
#     return fac
# j=fact(5)
# print(j)
# def fibonacchi(num,list,first,second):
#     if num==0:
#         return
#     if not list:
#         list.append(first)
#         list.append(second)
#     third=first+second
#     list.append(third)
#     first=second
#     second=third
#     fibonacchi(num-1,list,first,second)
# list=[]
# fibonacchi(6,list,0,1)
# print(list)

# def fibonacchi(num):
#     list=[]
#     def Calculate(num,first,second):
#         if num==0:
#             return
#         if not list:
#             list.append(first)
#             list.append(second)
#         third=first+second
#         list.append(third)
#         first=second
#         second=third
#         Calculate(num-1,first,second)
#     Calculate(num,0,1)
#     return list
# j=fibonacchi(5)
# print(j)
# def reverse(number,n):
#     # print(rev)
#     if n==0:
#         return n
#     # rev=""
#     rev+=str(reverse(number,n-1))
#     return rev
# number="9876"
# n=len(number)
# j=""
# l=reverse(number,n)
# print(l)
#fibonacchi programme
# def fibonacchi(n):
#     f=[]
#     f.append(0)
#     f.append(1)
#     for i in range(2,7):
#         f.append(f[i-1]+f[i-2])
#     print(f)
import openai

# Set your OpenAI GPT-3 API key here
openai.api_key = 'YOUR_API_KEY'

def chat_with_gpt3(messages):
    # Format messages for input to the API
    conversation = [{'role': role, 'content': content} for role, content in messages]

    # Call the OpenAI API to generate a message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract and return the generated message
    reply = response['choices'][0]['message']['content']
    return reply

# Example conversation
conversation_history = [
    ("system", "You are a helpful assistant."),
    ("user", "Who won the world series in 2020?"),
    ("assistant", "The Los Angeles Dodgers won the World Series in 2020."),
    ("user", "Where was it played?"),
]

# Add a new user message to the conversation
new_user_message = ("user", "Tell me more about the venue.")
conversation_history.append(new_user_message)

# Get a reply from GPT-3 based on the updated conversation
response = chat_with_gpt3(conversation_history)

# Display the GPT-3 response
print(response)