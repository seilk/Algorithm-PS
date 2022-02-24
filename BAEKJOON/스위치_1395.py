import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def segInit(start, end, cur):
  global segtree, arr
  if start==end:
    segtree[cur][0] = arr[start][0]
    segtree[cur][1] = arr[start][1]
    return segtree[cur]
  mid=(start+end)//2
  left = segInit(start,mid,cur*2)
  right = segInit(mid+1,end,cur*2+1)
  segtree[cur][0]=left[0]+right[0]
  segtree[cur][1]=left[1]+right[1]
  return segtree[cur]

def update(start, end, cur, left, right):
  global lazy, segtree
  if lazy[cur]>0: # 반전하는 경우
    swp = segtree[cur][0]
    segtree[cur][0] = segtree[cur][1]
    segtree[cur][1] = swp
    if start!=end: # 전파
      lazy[cur*2] *= -1
      lazy[cur*2+1] *= -1
    lazy[cur]=-1 # 삭제
  if right<start or end<left :
    return
  if left<=start and end<=right:
    swp = segtree[cur][0]
    segtree[cur][0] = segtree[cur][1]
    segtree[cur][1] = swp
    if start!=end: # 레이지 자손 노드에 적용
      lazy[cur*2]*=-1
      lazy[cur*2+1]*=-1
    lazy[cur]=-1 # 삭제
    return
  # 걸쳐있을 경우
  mid = (start+end)//2
  update(start,mid,cur*2,left,right)
  update(mid+1,end,cur*2+1,left,right)
  segtree[cur][0] = segtree[cur*2][0] + segtree[cur*2+1][0]
  segtree[cur][1] = segtree[cur*2][1] + segtree[cur*2+1][1]

def find(start, end, cur, left, right):
  global lazy, segtree
  if lazy[cur]>0: # 반전하는 경우
    swp=segtree[cur][0]
    segtree[cur][0]=segtree[cur][1]
    segtree[cur][1]=swp
    if start!=end:
      lazy[cur*2]*=-1 # 반전 확산
      lazy[cur*2+1]*=-1 # 반전 확산
    lazy[cur]=-1
  if right<start or end<left:
    return 0
  if left<=start and end<=right:
    return segtree[cur][0] # 켜져있는 스위치 개수 return
  mid=(start+end)//2
  leftt=find(start,mid,cur*2,left,right) # 변수이름 주의 left, right
  rightt=find(mid+1,end,cur*2+1,left,right) # 변수 이름 주의 left, right
  return leftt+rightt

def solve(N,M):
  global segtree, arr, lazy
  arr=[[0,1] for i in range(N+1)] # [ON, OFF]
  segtree = [[0,0] for i in range(4*(N+1))]
  segInit(1,N,1)
  lazy = [-1]*(4*(N+1))
  for m in range(M):
    query = list(MIS())
    if query[0]==0:
      update(1,N,1,query[1],query[2])
    else:
      print(find(1,N,1,query[1],query[2]))

if __name__ == "__main__":
  N, M = MIS()
  solve(N,M)