import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def rec(cur,p):
  global res
  a=0;aa=0
  for n,w in grp[cur]:
    if n!=p:
      k=w+rec(n,cur)
      if k>a : aa=a; a=k
      elif k>aa: aa=k
  res=max(res,a+aa)
  return a

V=int(In())
grp=[[] for i in range(V+1)]
for v in range(V):
  infos=deque([*MIS()])
  a=infos.popleft()
  while 1:
    try:
      b=infos.popleft()
      c=infos.popleft()
      grp[a].append((b,c)) # 자식노드, 가중치
    except:
      break
res=0
rec(1,0)
print(res)

# 8
# 1 2 1 3 2 -1
# 2 1 1 4 3 5 4 -1
# 3 1 2 6 5 -1
# 4 2 3 -1
# 5 2 4 7 6 8 7 -1
# 6 3 5 -1
# 7 5 6 -1
# 8 5 7 -1