import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(x):
  if fr[x]==x:
    return x
  fr[x]=find(fr[x])
  return fr[x]

def union(x,y):
  a=find(x)
  b=find(y)
  if a == b:
    return
  if a>b:
    fr[a]==b
  else:
    fr[b]=a

N = int(In())
M = int(In())
fr=[i for i in range(N+1)]
ev=[0 for i in range(N+1)]
for m in range(M):
  s, a, b = In().split()
  a, b = map(int, [a,b])
  if s=="F":
    union(a,b)
  else:
    if ev[b]!=0:
      union(a,ev[b])
    if ev[a]!=0:
      union(b,ev[a])
    ev[a]=b
    ev[b]=a

vist=[0]*(N+1)
cnt=0
for i in range(1,N+1):
  j=find(i)
  if not vist[j]:
    vist[fr[i]]+=1
    cnt+=1

print(cnt)