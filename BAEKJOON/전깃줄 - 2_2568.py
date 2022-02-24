import sys
from collections import deque
from bisect import bisect_left, bisect_right
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
LL = int(In())
arr=[-1]*500_001
for l in range(LL):
  a, b = MIS()
  arr[a] = b
L=[]
P=[-1]*500_001
tot=0
for i in range (500_001):
  if arr[i] != -1:
    if not L:
      L.append(arr[i])
      tot+=1
      cur=1
    elif L[-1] < arr[i]:
      L.append(arr[i])
      tot+=1
      cur=tot
    else:
      idx=bisect_left(L, arr[i])
      L[idx]=arr[i]
      cur=idx+1
    P[i]=cur
LIS_length=tot
ANS=deque()
for i in range(500_000,-1,-1):
  if P[i]!=-1:
    if P[i]==tot:
      tot-=1
      continue
    elif P[i] != tot:
      ANS.appendleft(i)
ANS=list(ANS)
print(LL-LIS_length)
print(*ANS,sep="\n")


