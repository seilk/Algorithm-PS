import sys
def input(): return sys.stdin.readline().rstrip()


x = input()
y = input()
dp = [[0 for i in range(len(x) + 1)] for i in range(len(y) + 1)]
for i in range(1, len(y) + 1):
    for j in range(1, len(x) + 1):
        dp[i][j] = dp[i - 1][j - 1] + 1 if y[i - 1] == x[j -
                                                         1] else max(dp[i - 1][j], dp[i][j - 1])

for i in dp:
    print(*i)
print(dp[len(y)][len(x)])

# ACAYKP
# CAPCAK
# AXBXCXD
# ZABCD
# 최장 공통 부분 수열
# 단어 하나를 기준으로 ?
# 이전 LCS에서 + 1 을 해준다.
# 이전 LCS길이는 대각선 성분을 의미한다. why?
# x나 y가 따로 하나씩 추가된 상황에서는 새로운 LCS가 없다.
# x와 y가 각각 하나씩 추가된 상황에서만 새로운 LCS가 생길 가능성이 있다.
# 따라서 비교상황에서의 이전 LCS는 x와 y가 각각 하나씩 빠진 상황에서의 LCS이다.
#
# 처음 풀이
#import sys
# def input(): return sys.stdin.readline().rstrip()


# x = input()
# y = input()
# dp = [[0 for i in range(len(x) + 1)] for i in range(len(y) + 1)]
# for i in range(1, len(y) + 1):
#     for j in range(1, len(x) + 1):
#         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + \
#             1 if y[i - 1] == x[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
# # for i in dp:
# #     print(*i)
# print(dp[len(y)][len(x)])
