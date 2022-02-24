import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
T = int(In())
for t in range(T):
  N = int(In())
  arrA = [*MIS()]
  arrB = [*MIS()]
  MXX = 0
  for i in range(N):
    if arrA[i] > arrB[i]:
      swp = arrB[i]
      arrB[i] = arrA[i]
      arrA[i] = swp
    MXX = max(MXX, arrB[i])
  print(MXX*max(arrA))

