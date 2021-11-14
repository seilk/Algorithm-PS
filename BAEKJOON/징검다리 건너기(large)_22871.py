import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
bridge = list(map(int, input().split()))
dp = [0] * n
dp[1] = (1 - 0) * (1 + abs(bridge[1] - bridge[0]))
for i in range(2, n):
    tmp = [i * (1 + abs(bridge[i] - bridge[0]))]
    for j in range(1, i):
        energy = (i-j) * (1 + abs(bridge[i] - bridge[j]))
        tmp.append(max(dp[j], energy))
    dp[i] = min(tmp)  # i 돌다리 까지 오는데 최소 소모 에너지
print(dp[n - 1])
######
n = int(input())
A = list(map(int, input().split()))
power = [10**18]*n  # dp
power[0] = 0  # dp
for i in range(n-1):
    for j in range(i+1, n):
        taken = max(power[i], (j-i)*(1 + abs(A[i]-A[j])))
        power[j] = min(power[j], taken)
print(power[-1])

# [0] [1] [2] [3]

# import sys
# sys.setrecursionlimit(10 ** 9)


# def check(K):
#     dp = [False for _ in range(N)]
#     dp[0] = True
#     for i in range(N-1):
#         if dp[i]:
#             for j in range(i+1, N):
#                 tempK = (j-i)*(abs(arr[i]-arr[j])+1)
#                 if tempK <= K:
#                     dp[j] = True

#     return dp[N-1]


# def input():
#     return sys.stdin.readline().rstrip()


# N = int(input())

# arr = list(map(int, input().split()))
# left = 0
# right = 1000000

# while left+1 < right:
#     mid = (left+right)//2

#     if check(mid):
#         right = mid
#     else:
#         left = mid

# print(right)
