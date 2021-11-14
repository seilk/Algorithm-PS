import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
info = [[0, 0]] + [list(map(int, input().split())) for i in range(n)]
# 현재날짜 + [0] 이상의 날짜에서만 상담가능
# 현재날짜 + [0]이 퇴사날짜이상이면 상담불가능
maxVal = -1


def DFS(day, n, val):
  global maxVal
  if day >= n + 1:
      maxVal = max(maxVal, val)
      return
  for i in range(day, n + 1):
      if i + info[i][0] <= n + 1:  # 상담을 마치는 날이 퇴사날짜면 상담 가능
          DFS(i + info[i][0], n, val + info[i][1])
      else:
          DFS(day + 15, n, val)

  return maxVal


print(DFS(1, n, 0))
