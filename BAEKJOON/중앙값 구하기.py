import sys
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T = int(In())
for t in range(T):
  M = int(In())
  MAX = 1<<32+1
  left = [MAX]
  right = [MAX]
  arr=[0]
  for d in range(M//10):
    arr+=[*MIS()]
  arr+=[*MIS()]
  ans = [arr[1]]
  mid = arr[1]
  for m in range(2,M+1):
    if m&1:
      if arr[m]<=-left[0]:
        heappush(left, -arr[m])
        heappush(right, mid)
        mid = -heappop(left)
      elif -left[0]<arr[m]<=mid:
        if -left[0]==-MAX:
          heappush(left, -arr[m])
        else:
          heappush(left, -mid)
          mid = arr[m]
      elif mid<arr[m]<=right[0]:
        if right[0]==MAX:
          heappush(right, arr[m])
        else:
          heappush(left, -mid)
          mid = arr[m]
      elif right[0]<arr[m]:
        heappush(left, -mid)
        heappush(right, arr[m])
        mid = heappop(right)
      ans.append(mid)
    else:
      if arr[m] < mid:
        heappush(left, -arr[m])
      else:
        heappush(right, arr[m])
  print(M//2+1) if M%2 else print(M//2)
  div=M//10
  if div==0:
    print(*ans)
  else:
    a=0
    for p in range(1,div+1):
      print(*ans[a:10*p])
      a=10*p
    print(*ans[a:])
