import sys
sys.setrecursionlimit(10**5)
def updateplus(nodestart, nodeend, cur, target):
  if nodeend < target or target < nodestart:
    return
  segtree[cur]+=1
  if nodestart==nodeend:
    return
  mid = (nodestart+nodeend)//2
  updateplus(nodestart, mid, cur*2, target)
  updateplus(mid+1, nodeend, cur*2+1, target)

def updateminus(nodestart, nodeend, cur, target):
  if nodeend < target or target < nodestart:
    return
  segtree[cur]-=1
  if nodestart==nodeend:
    return
  mid = (nodestart+nodeend)//2
  updateminus(nodestart, mid, cur*2, target)
  updateminus(mid+1, nodeend, cur*2+1, target)

def find(nodestart, nodeend, cur, left, right):
  if nodeend < left or right < nodestart:
    return 0
  if left<= nodestart and nodeend <= right:
    return segtree[cur]
  mid=(nodestart+nodeend)//2
  return find(nodestart,mid,cur*2,left,right) + find(mid+1,nodeend,cur*2+1,left,right)

def segInit(start, end, cur):
  if start == end:
    segtree[cur] = arr[start]
    return segtree[cur]
  mid = (start+end)//2
  segtree[cur] = segInit(start, mid, cur*2) + segInit(mid+1, end, cur*2+1)
  return segtree[cur]

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
T = int(In())
for t in range(T):
  N, M = MIS()
  totBooks = N
  arr = [1]*(N+1) + [0]*M
  segtree = [0]*(N+M+1)*4
  query = list(MIS())
  ansSet = []
  segInit(1,N+M,1)
  dvd = [0]+[N-i for i in range(N)]
  top = N
  for q in query:
    #find
    pre = dvd[q] # 몇층에 있는지 확인
    ansSet.append(find(1, N+M, 1, pre+1, N+M))
    #update
    dvd[q] = top+1
    arr[pre]=0
    arr[dvd[q]]=1
    updateplus(1, N+M, 1, top+1)
    updateminus(1, N+M, 1, pre)
    top+=1
  print(*ansSet)