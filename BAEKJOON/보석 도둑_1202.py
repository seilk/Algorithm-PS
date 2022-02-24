# ----------Title
# 보석 도둑
# Gold II
# https://boj.kr/1202

# ----------Tip
# Greedy
# heap

# ----------URLs
# https://jaimemin.tistory.com/760

# ----------Code with Detail
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, K = map(int, input().split())
jw = []
for i in range(N):
  M, val = map(int, input().split())
  jw.append((M, val))
jw.sort(key=lambda x: x[0])
bags = [int(input().rstrip()) for i in range(K)]
bags.sort(reverse=True)

# 가방과 보석 매칭
ans = 0
s = -1
tmp = []

while bags:
  C = bags.pop()
  for i in range(s + 1, N):
    if C >= jw[i][0]:
      heappush(tmp, (-jw[i][1], jw[i][0]))
      s = i
    else:
      break

  # 정답출력
  if tmp:
    val, M = heappop(tmp)
    ans += -val
print(ans)
# 2 2
# 5 5
# 5 5
# 1
# 10
#
# 4 3
# 2 400
# 5 200
# 3 67
# 4 30
# 3
# 6
# 5
#
# 3 2
# 4 65
# 5 23
# 2 99
# 9
# 1
#
# 4 4
# 1 100
# 2 200
# 13 300
# 10 500
# 10
# 10
# 10
# 14
#
