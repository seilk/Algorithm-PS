# ----------Title
# 추월
# Silver I
# https://boj.kr/2002 

# ----------Tip

# ----------URLs

# ----------Code with Detail
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n = int(input())
inn = defaultdict(int)
outt = defaultdict(int)
tmp = []
for i in range(n):
  car = input()
  inn[car] = i  # in
  tmp.append(car)  # 들어온 차 정렬
for i in range(n):
  outt[input()] = i  # out

ans = 0
for i in range(1, n):  # 1등은 추월못함
  cname = tmp[i]
  idx = inn[cname]  # 들어갈때 index
  for tc in tmp[:idx]:  # 조사하는 차보다 먼저 들어간 차들의 outidx 전부 조사
    if outt[tc] > outt[cname]:
      ans += 1  # tc당 한번만 검사
      break
print(ans)

# ----------CounterExample
4
A
B
C
D
D
A
C
B
