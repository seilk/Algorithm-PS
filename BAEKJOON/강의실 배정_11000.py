import sys
from heapq import heappush, heappop, heapreplace
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N=int(In())
cls=[]
for n in range(N):
  heappush(cls, tuple(MIS())) #시작값이 작은 순서로 push

x=[]
while cls:
  a,b=heappop(cls) #강의의 시작시간, 종료시간
  if not x:
    heappush(x,b) #강의의 종료시간을 push
  else:
    if x[0]<=a:
      # heappop(x) #해당 강의의 종료시간을
      # heappush(x,b) #새로운 강의의 종료시간으로 갱신
      heapreplace(x,b)
    else:
      heappush(x,b)
print(len(x))