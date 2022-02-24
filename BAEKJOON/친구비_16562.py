# ----------Title
# 친구비
# Gold III
# https://www.acmicpc.net/problem/16562

# ----------Tip
# Union-Find
#

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**5)


def find(x):
  if p[x] < 0:
    return x
  p[x] = find(p[x])  # 친구의 친구는 친구!
  return p[x]


def union(x, y):
  a = find(x)
  b = find(y)
  if a == b:
    return
  if A[a] < A[b]:  # 더 작은 돈으로 묶을 수 있으면 작은 돈으로 집합을 묶는다.
    A[b] = 10001
    p[a] += p[b]
    p[b] = a
  else:
    A[a] = 10001
    p[b] += p[a]
    p[a] = b


def isFriend(k):
  global ans
  ans = 0
  for a in A:
    if a != 10001:
      ans += a

  if ans > k:  # 최소 친구비가 k보다 클 때
    return False
  return True


def solve():
  global ans
  for i in range(m):
    x, y = map(int, input().split())
    union(x, y)

  ans = 0
  if not isFriend(k):
    print("Oh no\n")
  else:
    print(str(ans) + "\n")


if __name__ == "__main__":
  n, m, k = map(int, input().split())
  p = [0] + [-1] * n
  A = [0] + [money for money in list(map(int, input().split()))]
  ans = 0
  solve()
