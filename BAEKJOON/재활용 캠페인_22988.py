import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N,X = MIS()
arr=[*MIS()]
arr.sort()
ans=0
for i in range(N-1,-1,-1):
  if arr[i] == X:
    arr.pop()
    ans+=1
l=0
r=len(arr)-1
rem=0
while l<=r:
  if l==r:
    rem+=1
    break
  if arr[l]+arr[r]>=X/2:
    r-=1
    l+=1
    ans+=1
  else:
    l+=1
    rem+=1
print(ans+(rem)//3)