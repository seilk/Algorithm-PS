import re

n = int(input())

for _ in range(n):
  s = input()
  p = re.compile('(100+1+|01)+')
  m = re.fullmatch(p, s)
  if m:
    print("YES")
  else:
    print('NO')
