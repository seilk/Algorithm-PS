import sys


def checkDotori(curBoxIdx):
  curDotori = 0
  for start, end, gap in query:
    if curBoxIdx >= start: # 현재 보고 있는 박스가 쿼리의 시작값보다 작을 수 있음.
      curDotori += ((min(curBoxIdx, end) - start) // gap) + 1  # gap을 나눈 몫을 이용해서 누적합을 O(1)에 계산하는 방법
  return curDotori >= D  # 현재 보고 있는 박스의 도토리 개수를 D와 비교


def solve():
  lo = 1
  hi = N
  while lo <= hi:
    mid = (hi + lo) // 2
    if checkDotori(mid):
      res = mid
      hi = mid - 1
    else:
      lo = mid + 1
  print("%s" % res)


if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  MIS = lambda: map(int, R().split())
  print = sys.stdout.write
  N, K, D = MIS()
  query = []
  for k in range(K):
    query.append(tuple(MIS()))
  solve()
