# ----------Title
# 성냥개비
# Gold II
# https://www.acmicpc.net/problem/3687


# ----------Tip
# Greedy
# DP

# ----------URLs


# ----------Code with Detail
import sys


def maxx(n):
  if n % 2 == 0:
    return "1" * (n // 2)
  if n % 2 == 1:  # 11 -> 4 * 2 + 3 -> 71111
    return "7" + "1" * ((n // 2) - 1)


def minn(n):
  if n == 6:
    return "6"
  INF = "8888888888888"
  dp = [INF, INF, "1", "7", "4", "2", ("0", "6"), "8"] + [INF] * (n - 7)
  if n >= 8:
    dp[8] = "10"

  # 11 -> 6 + 5 / 7 + 4 / 8 + 3 / 9 + 2 /
  # 12 -> 6 + 6
  for i in range(9, n+1):
    for j in range(2, ((n+1)//2) + 1):
      if i - j == j == 6:
        dp[i] = str(min(int(dp[i]),
                        int(dp[j][1] + dp[i - j][0]),
                        int(dp[i - j][1] + dp[j][0])))
      elif i - j == 6:
        dp[i] = str(min(int(dp[i]),
                        int(dp[j] + dp[i - j][0]),
                        int(dp[i - j][1] + dp[j])))
      elif j == 6:
        dp[i] = str(min(int(dp[i]),
                        int(dp[j][1] + dp[i - j]),
                        int(dp[i - j] + dp[j][0])))
      else:
        dp[i] = str(min(int(dp[i]),
                        int(dp[j] + dp[i - j]),
                        int(dp[i - j] + dp[j])))

  # print(dp)
  return dp[n]


if __name__ == "__main__":
  input = sys.stdin.readline
  printt = sys.stdout.write
  tc = int(input().rstrip())
  for _ in range(tc):
    n = int(input().rstrip())
    printt(minn(n) + " " + maxx(n) + "\n")
