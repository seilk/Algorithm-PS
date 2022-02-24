import sys
from itertools import permutations

year, d = map(int, input().split())
INF = float("inf")
tmp = [str(i) for i in range(d)]
tmpp = list(permutations(tmp, d))
mnn = INF
for item in tmpp:
  if item[0] == '0':
    continue
  k = int("".join(item), d)
  if k > year:
    if k < mnn:
      mnn = k
if mnn == INF:
  print(-1)
else:
  print(mnn)
