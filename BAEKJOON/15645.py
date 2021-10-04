import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline()


def findMin(row, col):  # dp Memoization
    if dp[row][col] == -1:
        if row == n:
            return 0

        if col == 0:
            dp[row][col] = board[row][col] + \
                min(findMin(row + 1, col), findMin(row + 1, col + 1))

        elif col == 2:
            dp[row][col] = board[row][col] + \
                min(findMin(row + 1, col), findMin(row + 1, col - 1))

        elif col == 1:
            dp[row][col] = board[row][col] + min(findMin(row + 1, col), findMin(row + 1, col - 1),
                                                 findMin(row + 1, col + 1))
        return dp[row][col]
    return dp[row][col]


def findMax(row, col):
    if dp[row][col] == -1:  # dp Memoization
        if row == n:
            return 0

        if col == 0:
            dp[row][col] = board[row][col] + \
                max(findMax(row + 1, col), findMax(row + 1, col + 1))

        elif col == 2:
            dp[row][col] = board[row][col] + \
                max(findMax(row + 1, col), findMax(row + 1, col - 1))

        elif col == 1:
            dp[row][col] = board[row][col] + max(findMax(row + 1, col), findMax(row + 1, col - 1),
                                                 findMax(row + 1, col + 1))
        return dp[row][col]
    return dp[row][col]


n = int(input().rstrip())
board = [list(map(int, input().split())) for i in range(n)]
board += [0 for i in range(n)]
dp = [[-1 for i in range(3)] for i in range(n + 1)]
# for i in range(n , -1 , 0):
#     for j in range(n):
#         mini = min()
#         dp[i].append()

for i in range(3):
    findMax(0, i)
# print(dp)
print(max(dp[0]))

dp = [[-1 for i in range(3)] for i in range(n + 1)]

for i in range(3):
    findMin(0, i)
# print(dp)
print(min(dp[0]))
