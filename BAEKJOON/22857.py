# 시간 초과
import sys
from itertools import combinations
input = sys.stdin.readline
l, d = map(int, input().split())
srs = list(map(int, input().split()))
srs_e = []
for i in range(d + 1):  # 삭제하지 않는 경우 ~ 최대로 삭제하는 경우
    k = l - i
    srs_e += list(combinations(srs, k))

maxValue = 0
for lst in (srs_e):
    dp = [0 for i in range(len(lst))]
    dp[0] = 1 if (lst[0] % 2 == 0) else 0  # 초기값 세팅
    for i in range(1, len(lst)):
        if (lst[i] % 2 == 0):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    maxValue = max(maxValue, max(dp))

print(maxValue)


# p = [1, 2, 3, 4, 5, 6]
# print(list(combinations(p, 4)))
