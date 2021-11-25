# ----------Title
# 최대 힙
# Silver II
# https://boj.kr/11279

# ----------Tip
# 우선순위 큐 (Priority Queue)
# python heapq는 최소 heap만 지원한다.

# ----------URLs

# ----------Code with Detail
import sys
from heapq import heappop, heappush
def input(): return sys.stdin.readline().rstrip()


n = int(input())
p = []
for i in range(n):
  x = int(input())
  try:
    print(-heappop(p)) if x == 0 else heappush(p, -x)
  except(IndexError):
    print(0)
