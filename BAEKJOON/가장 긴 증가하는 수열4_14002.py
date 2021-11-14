import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
series = list(map(int, input().split()))
dp = [1] * n
ans = [[i] for i in series]
for i in range(1, n):
  for j in range(i):
    if series[j] < series[i]:
      if dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1
        ans[i] = ans[j] + [series[i]]
print(max(dp))
print(*max(ans, key=lambda x: len(x)))


# from collections import deque
# N = int(input())
# A = list(map(int, input().split()))
# dp = [1] * N 
# Alist = [[i] for i in A] 
# #[1, 2, 2, 3, 1]
# #[[10], [10, 20], [10, 15], [10, 15, 17], [10, 15, 17, 50]]
# #[10, 20, 15, 17, 50]

# for i in range(N):
#     # tmp = []
#     for j in range(i):# 1
#         if A[j] < A[i]: #20 < 15
#             if dp[j]+1 > dp[i]: # 2 > 1
#                 dp[i] = dp[j]+1 
#                 Alist[i] = Alist[j] + [A[i]] # [10, 15] + [17] = [10, 15, 17]
#     # tmp.append(A[i])
#     # Alist[i] = tmp

# print(max(dp))
# print(*Alist[dp.index(max(dp))])