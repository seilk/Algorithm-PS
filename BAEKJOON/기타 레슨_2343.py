# 강의의 순서는 건드리면 안됨
#
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lessons = list(map(int, input().split()))
MIN = max(lessons)
MAX = 1_000_000_000
while MIN < MAX:  # LowerBound
  MID = (MIN + MAX) // 2
  cnt = 1
  SUM = 0
  # MAX 값을 변경할지 MIN 값을 변경할지 정해주는 for문
  for i in range(N):
    SUM += lessons[i]
    if SUM > MID:
      SUM = lessons[i]
      cnt += 1
  if cnt > M:
    MIN = MID + 1
  else:
    MAX = MID
print(MAX)
