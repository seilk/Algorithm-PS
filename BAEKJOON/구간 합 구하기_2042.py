# ----------Title
# 구간 합 구하기
# Gold I
# https://boj.kr/2042

# ----------Tip
# 세그먼트 트리

# ----------URLs


# ----------Code with Detail
import sys
import math


# 세그먼트 트리 만들어주기 (구간합을 저장하는 이진 트리)

# 재귀적으로 segment tree 만들어주기
def makesegtree(curnode, start, end):
  if start == end:
    segtree[curnode] = arr[start]
    return curnode
  mid = (start + end) // 2
  leftnode = makesegtree(curnode * 2, start, mid)
  rightnode = makesegtree(curnode * 2 + 1, mid + 1, end)
  segtree[curnode] = segtree[leftnode] + segtree[rightnode]
  return curnode


def changevalue(curnode, start, end, index, diff):
  if (index < start) or (end < index):
    return
  segtree[curnode] += diff
  if start != end:
    mid = (start + end) // 2
    changevalue(curnode * 2, start, mid, index, diff)  # change left
    changevalue(curnode * 2 + 1, mid + 1, end, index, diff)  # change right


def sumvalue(curnode, nodestart, nodeend, start, end):
  if start <= nodestart and nodeend <= end:  # 노드가 갖는 범위가 구하는 범위의 포함관계라면 그 세그먼트트리의 값을 리턴해서 더해줘야한다.
    return segtree[curnode]
  if (end < nodestart) or (nodeend < start):  # 범위가 전혀 맞지 않는 경우
    return 0
  mid = (nodestart + nodeend) // 2
  left_sum = sumvalue(curnode * 2, nodestart, mid, start, end)
  right_sum = sumvalue(curnode * 2 + 1, mid + 1, nodeend, start, end)
  return left_sum + right_sum


if __name__ == "__main__":
  sys.setrecursionlimit(10 ** 4)
  input = sys.stdin.readline
  N, M, K = map(int, input().split())
  arr = [int(input().rstrip()) for i in range(N)]  # 배열에 값 넣어주기

  segheight = int(math.ceil(math.log2(N)))  # 세그먼트 트리의 높이
  segsize = 1 << (segheight + 1)  # 세그먼트 트리의 사이즈(노드의 개수)
  segtree = [-1 for i in range(segsize)]  # 0번째 노드는 사용하지 않음

  makesegtree(1, 0, N - 1)

  # 합을 구해야하는 범위 횟수 or 수의 변경이 일어나는 횟수 받아오기
  for i in range(M + K):
    sign, x0, x1 = map(int, input().split())
    if sign == 1:  # 수 변경
      diff = x1 - arr[x0 - 1]
      arr[x0 - 1] = x1  # 차이를 구하고 난 다음 처음에 입력으로 받아온 arr에 대해서도 item을 변경해줘야함 (그래야 나중에 diff를 구할때 오차가 안생김)
      changevalue(1, 0, N - 1, x0 - 1, diff)
    elif sign == 2:  # 구간 합 구하기
      print(sumvalue(1, 0, N - 1, x0 - 1, x1 - 1))
