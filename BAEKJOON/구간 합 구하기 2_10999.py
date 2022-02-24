# lazy propagation : 느리게 갱신되는 세그먼트 트리
# 세그먼트 트리에서 한개의 값을 업데이트 하는데 걸리는 시간 O(logN)
# 구간의 값을 업데이트 해야한다면 최악의 경우 O(NlogN)
# lazy를 사용하면 O(logN)에 모든 구간의 값을 업데이트 할 수 있다.
# 부모노드에 변화를 적용시킨 후 자식노드에 여지를 남기고 함수를 종료한다는 개념 - 완전 속하는 대표 노드를 발견하면 함수종료됨
# 이후 update와 find를 실행시킬때 lazy가 존재하는 모든 노드에서는 lazy를 반영-전파-삭제한 뒤 이어서 작업을 수행
# segsum을 해줄때나 segupdate를 해줄때나 lazy가 존재하는 노드에서는 lazy를 반영-전파-삭제 하는 과정 실행
# !주의 : lazy가 음수일 경우가 있음
# https://bowbowbow.tistory.com/4
import sys

def segInit(start, end, cur):
  global segtree
  if start == end:
    segtree[cur] = arr[start]
    return segtree[cur]
  mid = (start+end)//2
  segtree[cur] =segInit(start,mid,cur*2)+segInit(mid+1,end,cur*2+1)
  return segtree[cur]

def update(start, end, cur, left, right, diff):
  if lazy[cur]!=0:
    # 업데이트 할 때 마다 지나가는 부모노드의 lazy는 항상 반영-전파-삭제해야함
    # 어느 구간에서든지 lazy가 남아있는 경우에는 자기 자신의 값을 갱신하고 자식 노드에 lazy를 전파한다.
    # 이렇게 하지 않으면 완전 속하는 구간을 찾을때 부모 노드의 lazy가 반영되지 않을 수 있다.
    segtree[cur]+=lazy[cur]*(end-start+1)
    if start!=end:
      lazy[cur*2]+=lazy[cur]
      lazy[cur*2+1]+=lazy[cur]
    lazy[cur]=0
  if right<start or end<left:
    return
  if left<=start and end<=right:
    # 완전히 속하는 구간에서는 대표 노드만 값을 갱신하고 자식 노드에는 lazy로 전달한다.
    segtree[cur]+=diff*(end-start+1) # diff에 의한 변화, lazy에 의한 변화랑 혼동X
    if start!=end:
      lazy[cur*2]+=diff
      lazy[cur*2+1]+=diff
    lazy[cur]=0
    return
  mid = (start+end)//2
  update(start,mid,cur*2,left,right,diff)
  update(mid+1,end,cur*2+1,left,right,diff)
  segtree[cur] = segtree[cur*2] + segtree[cur*2+1]

def find(start, end, cur, left, right):
  if lazy[cur]!=0:
    segtree[cur]+=lazy[cur]*(end-start+1) # 현재노드에 lazy 반영 후
    if start != end: # 자식노드가 있을 때
      lazy[cur*2]+=lazy[cur]
      lazy[cur*2+1]+=lazy[cur] # 자식노드에 전파
    lazy[cur]=0 # 삭제
  if right<start or end<left:
    return 0
  if left<=start and end<=right:
    return segtree[cur]
  mid = (start+end)//2
  return find(start,mid,cur*2,left,right)+find(mid+1,end,cur*2+1,left,right)


def solve(arr, N):
  global segtree, lazy
  segtree=[0]*(4*N)
  lazy=[0]*(4*N)
  segInit(1,N,1) # 세그먼트 트리 초기화
  for q in range(Q+S):
    query = list(MIS())
    if query[0] == 1:
      update(1, N, 1, query[1], query[2], query[3])
    else:
      print(find(1, N, 1, query[1], query[2]))

if __name__ == "__main__":
  In = lambda : sys.stdin.readline().rstrip()
  MIS = lambda : map(int, In().split())
  N, Q, S = MIS()
  arr=[0]+[int(In()) for i in range(N)]
  solve(arr, N)