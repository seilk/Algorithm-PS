import sys
R = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, R().split())
N, S = MIS()
arr = [*MIS()]
prefix = [arr[0]] + [0 for i in range(N-1)]
for i in range(1, N):
  prefix[i] = prefix[i-1] + arr[i]
start, end = 0,0
mnn = 100_001
while start < N and end < N:
  if start == end:
    SUM = arr[start]
  else:
    SUM = prefix[end] - prefix[start] + arr[start]

  if SUM < S:
    if end == N - 1:
      break
    end += 1
  else:
    length = end - start + 1
    if mnn > length:
      mnn = length
      if mnn == 1:
        break
    start += 1
if mnn == 100_001:
  print(0)
else:
  print(mnn)