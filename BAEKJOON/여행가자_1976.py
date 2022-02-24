# ----------Title
# 여행가자
# Gold IV
# https://boj.kr/1976

# ----------Tip
# Union-Find

# ----------URLs
# https://bowbowbow.tistory.com/26

# ----------Code with Detail
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline  # input Overriding
print = sys.stdout.write  # print Overriding


def find(x):
  if p[x] < 0:
    return x
  p[x] = find(p[x])
  return p[x]


def merge(x, y):
  a = find(x)
  b = find(y)
  if a == b:
    return

  if p[a] < p[b]:
    p[a] += p[b]
    p[b] = a
  else:
    p[b] += p[a]
    p[a] = b


def solve(m):
  for c in range(1, m):
    if std != find(trip[c]):
      print("NO\n")
      return
  print("YES\n")
  return


if __name__ == "__main__":
  # Setting
  n = int(input().rstrip())
  m = int(input().rstrip())
  p = [-1] * (n + 1)  # 0번째 도시는 Dummy

  for i in range(1, n + 1):
    tmp = ([0]) + list(map(int, input().rstrip().split()))
    for j in range(2, n + 1):
      if i != j:
        if tmp[j] == 1:
          merge(i, j)

  trip = list(map(int, input().rstrip().split()))
  std = find(trip[0])
  solve(m)
