import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

#read사용, asterisk unpacking
#n,*arr = map(int,sys.stdin.read().split())
N = int(In())
arr=deque([(v,i) for i, v in enumerate([*MIS()])])
s=[]
ans=[-1]*(N)
while arr:
  x,i=arr.popleft()
  if not s: s.append((x,i)); continue;
  else:
    while s and s[-1][0]<x:
      ans[s[-1][1]]=x
      s.pop()
    s.append((x,i)); continue;
print(*ans)