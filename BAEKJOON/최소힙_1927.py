# ----------Title
# 최소 힙
# Silver I
# https://boj.kr/1927

# ----------Tip
# 우선순위 큐 (Priority Queue)
# python heapq는 최소 heap만 지원한다.

# ----------URLs

# ----------Code with Detail
import sys
from heapq import heappop, heappush
def input(): return sys.stdin.readline().rstrip()


p = []
for i in range(int(input())):
  x = int(input())
  try:
    print(heappop(p)) if x == 0 else heappush(p, x)
  except(IndexError):
    print(0)
