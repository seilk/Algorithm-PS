import sys
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
T = int(In())


def getArray():
  arr=[0]
  for d in range(M // 10):
    arr += [*MIS()]
  arr += [*MIS()]
  return arr


for t in range(T):
  M = int(In())
  MAX = 1<<32 + 1
  left = [MAX]
  right = [MAX]
  ll,rr=0,0
  arr = getArray()
  ans = [arr[1]]
  mid = arr[1]
  for m in range(2,M+1):
    if m&1:
      if arr[m]<=-left[0]: # 구간 1
        if ll<rr:
          heappush(left, -arr[m])
          ll+=1
        else:
          heappush(left, -arr[m])
          heappush(right, mid)
          rr+=1
          mid = -heappop(left)

      elif -left[0]<arr[m]<=mid: # 구간 2
        if -left[0]==-MAX:
          heappush(left, -arr[m])
          ll+=1
        else:
          if ll < rr:
            heappush(left, -arr[m])
            ll+=1
          else:
            heappush(right, mid)
            mid = arr[m]
            rr+=1

      elif mid<arr[m]<=right[0]: # 구간 3
        if right[0]==MAX:
          heappush(right, arr[m])
          rr+=1
        else:
          if ll>rr:
            heappush(right,arr[m])
            rr+=1
          else:
            heappush(left, -mid)
            ll+=1
            mid = arr[m]

      elif right[0]<arr[m]: # 구간 4
        if rr<ll:
          heappush(right,arr[m])
          rr+=1
        else:
          heappush(left, -mid)
          ll+=1
          heappush(right, arr[m])
          mid = heappop(right)
      ans.append(mid)

    else: #짝수 일 때
      if arr[m] < mid:
        heappush(left, -arr[m])
        ll+=1
      else:
        heappush(right, arr[m])
        rr+=1

  print((M//2)+1)
  div=((M//2)+1)//10
  if div==0:
    print(*ans)
  else:
    a=0
    for p in range(1,div+1):
      print(*ans[a:(10*p)])
      a=10*p
    if a < M//2+1:
      print(*ans[a:])

# 1
# 31
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29 30
# 31

# 1
# 11
# -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
# 100

# 1
# 5
# -2147483648 2147483648 -2147483648 -2147483648 -2147483648

# 1
# 19
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19

# 3
# 21
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19
# 20 21
# 31
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29 30
# 31
# 19
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19