import sys
from heapq import *
from collections import defaultdict

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T=int(In())
for t in range(T):
  K=int(In())
  dix=defaultdict(int) # 정수가 32비트라서 2^32개의 리스트를 만들수는 없다.
  maxq=[] #최대힙
  minq=[] #최소힙
  for k in range(K):
    cmd, num = In().split()
    num=int(num)
    if cmd == "I":
      heappush(maxq, -num)
      heappush(minq, num)
      dix[num]+=1
    if cmd == "D" and num == 1:
      while maxq:
        v = -heappop(maxq)
        if dix[v]==0: continue
        else: dix[v]-=1; break
    if cmd == "D" and num == -1:
      while minq:
        v = heappop(minq)
        if dix[v]==0: continue
        else: dix[v]-=1; break
  ans = []
  while maxq:
    ansMax = -heappop(maxq)
    if dix[ansMax]>0: # 이 부분에서 maxq[0]을 바라본다면 indexError가 날 수 있다.
      ans.append(ansMax)
      break
  while minq:
    ansMin = heappop(minq)
    if dix[ansMin]>0:
      ans.append(ansMin)
      break
  if len(ans)!=2:
    print("EMPTY")
  else: print(*ans)