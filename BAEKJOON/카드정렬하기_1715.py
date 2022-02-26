import sys
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
hq = []
for n in range(N): heappush(hq, int(In()))
ans=0
while hq:
  a=heappop(hq)
  if hq:
    b=heappop(hq)
    ans+=a+b
    heappush(hq, a+b)
print(ans)