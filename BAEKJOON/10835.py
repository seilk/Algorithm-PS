# ???
from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 6)
input = stdin.readline
n = int(input().rstrip())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
left.insert(0, 0)
right.insert(0, 0)

case1, case2 = 0, 0


def card(l, r):
    global case1, case2
    if l >= n + 1 or r >= n + 1:
        return 0

    if right[r] < left[l]:
        # r번째 오른쪽카드를 더하는 경우에는 r + 1번째 오른쪽 카드와 l번째 왼쪽카드를 비교해야한다.
        case1 = right[r] + card(l, r + 1)
    else:
        # 어느 방향으로든 갈 수 있다.(오른쪽만 버리는 경우 제외)
        case2 = max(card(l + 1, r + 1), card(l + 1, r))
    dp[l][r] = max(case1, case2)
    return dp[l][r]


card(0, 0)
print(dp[1][1])


# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if left[i] > right[j]:
#             dp[i][j] = max(dp[i][j - 1] + right[j], dp[i - 1][j],
#                            dp[i - 1][j - 1])

#         else:
#             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])

# sol = dp[n][n]

# print(sol)
