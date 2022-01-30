# merge sort tree : segmentTree의 확장버전
# 최소값, 최대값 구해서 세그먼트 트리 돌리는 것보다 더 시간빠름
# 트리가 어디까지 들어갈 가능성이 있는지 계산해보면 됨
import sys
from bisect import bisect_right
def init(start, end, curnode):
  if start==end:
    segtree[curnode] = [arr[start]]
    seglen[curnode] = 1
    return segtree[curnode], seglen[curnode]
  mid = (start + end) // 2
  left = init(start, mid, curnode*2)
  right = init(mid+1, end, curnode*2+1)
  segtree[curnode] = sorted(left[0]+right[0])
  seglen[curnode] = left[1]+right[1] # find에서 O(N)을 줄이기 위해 미리 구해줌
  return segtree[curnode], seglen[curnode]

def find(target, nodestart, nodeend, start, end, curnode):
  global ans
  if end < nodestart or nodeend < start:
    return
  elif start <= nodestart and nodeend <= end:
    idx=bisect_right(segtree[curnode], target)
    ans += seglen[curnode] - idx
    return
  mid=(nodestart+nodeend)//2
  if segtree[curnode*2][-1] > target:
    find(target, nodestart, mid, start, end, curnode*2)
  if segtree[curnode*2+1][-1] > target:
    find(target, mid+1, nodeend, start, end, curnode*2+1)

if __name__ == "__main__":
  In = lambda : sys.stdin.readline().rstrip()
  MIS = lambda : map(int, In().split())
  print = sys.stdout.write
  N = int(In())
  arr = [0] + [*MIS()]
  M = int(In())
  segtree = [[] for i in range(4*N)]
  seglen = [0]*(4*N)
  init(1,N,1)
  last_ans = 0
  for q in range(M):
    ans = 0
    a,b,c = MIS()
    i=a^last_ans
    j=b^last_ans
    k=c^last_ans
    find(k,1,N,i,j,1)
    print("%s" % ans + "\n")
    last_ans = ans
