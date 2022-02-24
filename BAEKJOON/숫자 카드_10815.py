import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input().rstrip())
arr = [*map(int, input().split())]
M = int(input().rstrip())
q = [*map(int, input().split())]
arr.sort()
for i in range(M):
  complete = False
  target = q[i]
  start = 0
  end = N - 1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] < target:
      start = mid + 1
    elif arr[mid] > target:
      end = mid - 1
    else:
      print("%s " % 1) if i < M - 1 else print("%s" % 1)
      complete = True
      break
  if not complete:
    print("%s " % 0) if i < M - 1 else print("%s" % 0)