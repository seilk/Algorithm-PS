# ----------Title
# 회의실 배정
# Silver II
# https://boj.kr/1931

# ----------Tip
# Greedy

# ----------URLs
# https://kim6394.tistory.com/67

# ----------Code with Detail
import sys
input = sys.stdin.readline
N = int(input().rstrip())
p = []
for i in range(N):
  st, et = map(int, input().split())
  p.append((st, et))
p.sort(key=lambda x: (x[1], x[0]))

st, et = 0, 0
ans = 0
for i in range(N):
  if et <= p[i][0]:
    et = p[i][1]
    ans += 1
print(ans)
