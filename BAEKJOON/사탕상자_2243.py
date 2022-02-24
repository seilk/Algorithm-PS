# 뽑고자 하는 사탕의 rank는 segsum으로 찾아낼 수 있다.
# 결과적으로 하나의 노드를 발견하는것이 목표인 문제
# 기본적으로 segtree에서 루트노드에서 왼쪽 노드는 루트노드가 포괄하는 범위에서 작은 인덱스 범위의 누적합, 오른쪽 노드는 높은 인덱스 범위의 누적합
# 이분적으로 생각해서 인덱스(순위)를 찾으려고 하는데 순위가 누적합 안에 포함되면 그 범위 안에 있다는 말이고 순위가 누적합보다 크면 그 범위 밖에 있다는 말이다.
# 이 과정을 리프 노드까지 진행
# 한번 찾을 때마다 update(세그합)
import sys
def update(targetnode, targetval, curnode, nodestart, nodeend):
  if nodestart > targetnode or targetnode > nodeend:
    return
  segtree[curnode]+=targetval
  if nodestart==nodeend:
    anss[curnode] = targetnode
    return
  mid = (nodestart+nodeend)//2
  update(targetnode, targetval, curnode * 2, nodestart, mid)
  update(targetnode, targetval, curnode * 2 + 1, mid + 1, nodeend)

def find(target, curnode, nodestart, nodeend):
  if nodestart==nodeend:
    return curnode
  mid = (nodestart+nodeend)//2
  if target <= segtree[curnode*2]:
    return find(target, curnode*2, nodestart, mid)
  else:
    return find(target-segtree[curnode*2], curnode*2+1, mid+1, nodeend)

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
n = int(In())
segtree=[0]*4_000_004
candy=[0]*1_000_001
anss = [0]*4_000_004
for _ in range(n):
  info=tuple(MIS())
  if info[0]==2:
    update(info[1], info[2], 1, 1, 1_000_000)
  else:
    ans=find(info[1], 1, 1, 1_000_000)
    print(anss[ans])
    update(anss[ans], -1, 1, 1, 1_000_000)

