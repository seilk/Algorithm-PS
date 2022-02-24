import sys
from heapq import heappush, heappop, heapreplace, heapify
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
hq=[*MIS()]
heapify(hq)

for r in range(N-1):
  hq=heapify([*MIS()])
  hq2=[]
  for t in range(N):
    heappush(hq2, tmp[t])
  for k in range(N):
    x=heappop(hq2)
    if x>hq[0]:
      heapreplace(hq, x)
print(heappop(hq))