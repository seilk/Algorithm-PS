import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N = int(In())
s=[]
ans=0
for i in range(N):
  cur=int(In())
  if not s:
    s.append([cur,1])
  else:
    while s and s[-1][0] < cur:
      x,y = s.pop()
      ans+=y
    if not s:
      s.append([cur,1])
      continue

    if s[-1][0]==cur:
      z=s[-1][1]
      ans+=z
      s.pop()
      if s:
        ans+=1
      s.append([cur,z+1])
      continue

    if s[-1][0] > cur:
      ans+=1
      # s.append([cur,1])
      continue

print(ans)
