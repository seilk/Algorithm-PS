# ----------Title
# 합 구하기
# Silver III
# https://boj.kr/11441

# ----------Tip
# 부분 합

# ----------URLs


# ----------Code with Detail
import sys
import math

sys.setrecursionlimit(10 ** 4)


def makesegtree(curnode, start, end):
  if start == end:
    segtree[curnode] = arr[start]
    return segtree[curnode]  # 노드를 return
  mid = (start + end) // 2
  left_result = makesegtree(curnode * 2, start, mid)
  right_result = makesegtree(curnode * 2 + 1, mid + 1, end)
  segtree[curnode] = left_result + right_result
  return segtree[curnode]


def sumsegtree(curnode, nodestart, nodeend, start, end):
  # 완벽히 포함될 때
  if start <= nodestart and nodeend <= end:
    return segtree[curnode]
  # 완벽히 포함되지 않을 때
  if (nodestart > end) or (nodeend < start):
    return 0
  # 걸쳐있을 때
  mid = (nodestart + nodeend) // 2
  left_result = sumsegtree(curnode * 2, nodestart, mid, start, end)
  right_result = sumsegtree(curnode * 2 + 1, mid + 1, nodeend, start, end)
  return left_result + right_result


input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().split()))
M = int(input().rstrip())
segheight = math.ceil(math.log2(N))
segsize = 1 << (segheight + 1)
segtree = [-1 for i in range(segsize)]
makesegtree(1, 0, N - 1)
for i in range(M):
  x0, x1 = map(int, input().split())
  print(sumsegtree(1, 0, N - 1, x0 - 1, x1 - 1))
