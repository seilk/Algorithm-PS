import sys
from math import ceil, log2
sys.setrecursionlimit(10**3)

def makeSegtree(curnode, start, end):
  if start == end:
    segtree[curnode] = arr[start]
    return segtree[curnode]
  mid = (start + end) // 2
  makeSegtree(curnode * 2, start, mid)
  makeSegtree(curnode * 2 + 1, mid + 1, end)
  return


def update(curnode, nodestart, nodeend, START, END, diff):
  if nodeend < START or END < nodestart:
    return
  if START <= nodestart and nodeend <= END: # 구간에 완전히 속하면 현재 노드에 정해진 값을 더해준다.
    segtree[curnode] += diff
    return
  if nodestart != nodeend:
    mid = (nodestart + nodeend) // 2
    update(curnode * 2, nodestart, mid, START, END, diff)
    update(curnode * 2 + 1, mid + 1, nodeend, START, END, diff)
  return


def find(curnode, nodestart, nodeend, idx, ans):
  if idx < nodestart or nodeend < idx:
    return 0
  ans += segtree[curnode]
  if nodestart == nodeend:
    return ans
  mid = (nodestart + nodeend) // 2
  left = find(curnode * 2, nodestart, mid, idx, ans)
  right = find(curnode * 2 + 1, mid + 1, nodeend, idx, ans)
  return left + right

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
segheight = int(ceil(log2(N)))
segsize = 1 << (segheight + 1)
segtree = [0 for i in range(segsize)]
makeSegtree(1, 0, N - 1)
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    START, END, diff = query[1] - 1, query[2] - 1, query[3]
    update(1, 0, N - 1, START, END, diff)
  else:
    idx = query[1] - 1
    print(find(1, 0, N-1, idx, 0))
