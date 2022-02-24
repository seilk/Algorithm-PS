import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(r,c,l):
  visited[r][c]=1
  lst=deque([(r,c,-1)])
  k=[(0,-1),(-1,-1),(-1,0)]
  a=True
  cnt=-1
  b=1
  while a and lst:
    r,c,x=lst.popleft()
    for i in range(3):
      dr,dc=k[i]
      nr,nc=r+dr,c+dc
      if 0<=nr<n and 0<=nc<m and arr[nr][nc]==1:
        if not visited[nr][nc]:
          visited[nr][nc]=1
          if x>=0:
            if x==0 and nr==r and nc==c-1: lst.append((nr,nc,x))
            if x==1 and nr==r-1 and nc==c-1: lst.append((nr,nc,x))
            if x==2 and nr==r-1 and nc==c: lst.append((nr,nc,x))
          else: lst.append((nr,nc,i))
      else: a=False; break;
    if a:
      cnt+=1
      if cnt%3==0:
        l+=1
  return l

def search(r,c):
  for nr, nc in [(r-1,c-1),(r-1,c),(r,c-1)]:
    if arr[nr][nc]==0:
      return False
  return True

n,m=MIS()
arr=[[*map(int, list(In()))] for i in range(n)]
visited=[[0]*m for i in range(n)]
mxx=0
for r in range(n-1,-1,-1):
  for c in range(m-1,-1,-1):
    if not visited[r][c] and arr[r][c]==1:
      mxx=max((find(r,c,1))**2,mxx)
print(mxx)

# 3 4
# 1111
# 1110
# 1111
# 1111

# 3 4
# 1111
# 1101
# 1111

# 3 4
# 1110 # 3210 0 최소값 :
# 1110 # 2210 0 (+1) : 자기자신을 더함
# 1110 # 1110 0
# 1110 # 1110 0
# min+1


# 3 3
# 1111
# 1111
# 1111
# 1111


# 5 5
# 11111
# 10001
# 10001
# 10001
# 11111

# 5 5
# 00000
# 01100
# 01100
# 10001
# 11111

# 10 10
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 0000000000
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111