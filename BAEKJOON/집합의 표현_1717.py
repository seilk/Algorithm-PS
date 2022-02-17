# ----------Title
# 집합의 표현
# Gold IV
# https://boj.kr/1717

# ----------Tip
# Data Structure
# Disjoint Set
# Union_Find

# ----------URLs
# 1. https://bit.ly/3oRukya : Disjoint Set 설명
# 2. https://bit.ly/3DEvXpp : readline() 설명
# 3. https://www.acmicpc.net/board/view/37424 : sys.stdout.write() 알게됨

# ----------Code with Detail
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline  # 함수 지정보다 이게 더 빠름
# def input(): return  sys.stdin.readline().rstrip()  # 코드 꼬여서 지정 안해주는 실수함.
n, m = map(int, input().split())
p = [-1] * (n + 1)  # 자기자신의 Root를 기록한 Array


def find(n):  # 두 원소가 같은 root를 갖는지(같은 집합인지) 확인해주는 함수
  if p[n] < 0:
    return n  # p[root]는 음수
  p[n] = find(p[n])  # 재귀반복을 줄여주는 line, 직선상에서 같은 root를 갖고 있다면 root를 새로 갱신해줌
  return p[n]  # return 3 -> 4의 root가 3


def union(x, y):  # 두 집합을 합치는 func => 두 가지 root중 임의의 root로 묶기
  a = find(x)  # root search 1
  b = find(y)  # root search 2
  if a == b:
    return  # 이미 a,b의 root가 동일하면 새로 작업해줄 필요 X

  if p[a] > p[b]:  # 더 큰 Rank가 부모노드가 되게끔 하는 작업
    p[b] += p[a]
    p[a] = b
  else:
    p[a] += p[b]
    p[b] = a


for _ in range(m):
  c, x, y = map(int, input().split())
  if c == 0:  # union
    union(x, y)
  else:
    if x == y:
      sys.stdout.write("YES\n")
      continue
    sys.stdout.write("YES\n") if find(x) == find(y) else\
        sys.stdout.write("NO\n")

# ---------- TEST : 효율 3rd
sys.setrecursionlimit(10 ** 5)


def solve():
  n, m = map(int, sys.stdin.readline().split())
  p = [-1] * (n + 1)  # 자기자신의 Root를 기록한 Array

  def find(n):  # 두 원소가 같은 root를 갖는지(같은 집합인지) 확인해주는 함수
    if p[n] < 0:
      return n  # p[root]는 음수
    p[n] = find(p[n])  # 재귀반복을 줄여주는 line, 직선상에서 같은 root를 갖고 있다면 root를 새로 갱신해줌
    return p[n]

  def union(x, y):  # 두 집합을 합치는 func => 두 가지 root중 임의의 root로 묶기
    a = find(x)  # root search 1
    b = find(y)  # root search 2
    if a == b:
      return  # 이미 a,b의 root가 동일하면 새로 작업해줄 필요 X
    if p[a] > p[b]:  # 효율성 증가, 음수 value 비교 주의ㄴ
      p[b] += p[a]
      p[a] = b
    else:
      p[a] += p[b]
      p[b] = a

  for _ in range(m):
    c, x, y = map(int, sys.stdin.readline().split())
    if c == 0:  # union
      union(x, y)
    else:
      if x == y:
        sys.stdout.write("YES\n")
        continue
      sys.stdout.write("YES\n") if find(
          x) == find(y) else sys.stdout.write("NO\n")


solve()

#---------- TEST
# import sys
# import collections
# data = collections.defaultdict(set)
# def input(): return sys.stdin.readline().rstrip()


# n, m = map(int, input().split())

# for _ in range(m):
#   c, x, y = map(int, input().split())
#   if c == 0:  # 집합을 합치는 command
#     data[x].add(x)
#     data[y].add(y)

#     tmp0 = set() | data[x]  # {} or {x} = data[x]의 deepcopy
#     data[x] = tmp0 | data[y]
#     data[y] = tmp0 | data[y]
#   elif c == 1:  # 집합에서 원소의 여부를 확인하는 command
#     flg = False
#     for val in [data[x], data[y]]:
#       if (val & {x, y}) == {x, y}:
#         flg = True
#         break
#     if flg:
#       print("YES")
#     else:
#       print("NO")


# ---------- PRACTICE : 집합 deepcopy
# x = {1, 2, 3}
# tmp = set() | x
# x.discard(2)
# print(x)
# print(tmp)
# print({1, 2, 3} == {2, 1, 3})
