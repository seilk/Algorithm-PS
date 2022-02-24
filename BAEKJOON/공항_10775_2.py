import sys
sys.setrecursionlimit(10**5)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(x):
  if x<=0:
    return -1
  if not vist[x]:
    vist[x]=1
    return airport[x]
  airport[x] = find(airport[x])
  return airport[x]

G = int(In())
P = int(In())
airport = [i-1 for i in range(G+1)]
vist = [0]*(G+1)
ans=0
for p in range(P):
  g=int(In())
  fg=find(g)
  if fg==-1:
    print(ans)
    sys.exit(0)
    break
  ans+=1
print(ans)