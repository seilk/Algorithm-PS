import sys
from bisect import bisect_left, bisect_right, bisect
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
if __name__=="__main__":
  N=int(In())
  arr=[*MIS()]
  L=[]
  ans=0
  for i in range(N):
    if not L:
      L.append(arr[i])
      ans+=1
      continue
    elif L[-1] < arr[i]:
      L.append(arr[i])
      ans+=1
    else:
      L[bisect_left(L,arr[i])]=arr[i]
  print(N-ans)