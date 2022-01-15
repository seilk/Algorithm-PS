import sys


def isPalindrome(i, j):
  check[i][j] = 1
  if i == j:
    dp[i][j] = 1
    return
  left, right = i, j
  while left < right:
    if arr[left] != arr[right]:
      dp[i][j] = 0
      return
    left += 1
    right -= 1
  dp[i][j] = 1


input = sys.stdin.readline
N = int(input().rstrip())
arr = input().rstrip().split()  # 스트링 타입으로 저장
dp = [[0] * N for i in range(N)]
check = [[0] * N for i in range(N)]
Q = int(input().rstrip())

for i in range(Q):
  start, end = map(int, input().split())
  if check[start-1][end-1]: # 아직 확인을 안해본 구간일 때
    print(dp[start - 1][end - 1])
  else:
    isPalindrome(start-1, end-1)
    print(dp[start - 1][end - 1])
