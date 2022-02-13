import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N=int(In())
left=[]
x=int(In())
right=[]
print(x)

y=int(In())
print(x) if y>x else print(y)
z=int(In())

lst=sorted([x,y,z])
heappush(left,-lst[0])
heappush(right,lst[2])
mid=lst[1]
print(mid)

#3개를 완성시키고 짝수, 홀수로 구분하고
#인풋이 들어올 수 있는 4가지 구간에 따라서 조건 완성
for i in range(4,N+1):
  c=int(In())
  swp=mid
  if i%2: #부른 숫자가 홀수개 일 때
    if c< -left[0]:
      heappush(left,-c)
    elif -left[0]<=c<mid:
      heappush(left,-c)
    elif mid<=c<right[0]:
      mid=c
      heappush(left,-swp)
    elif right[0]<=c:
      mid=heappop(right)
      heappush(left,-swp)
      heappush(right,c)

  else: #부른 숫자가 짝수개 일 때
    if c < -left[0]:
      mid=-heappop(left)
      heappush(left,-c)
      heappush(right,swp)
    elif -left[0]<=c<mid:
      mid=c
      heappush(right,swp)
    elif mid<=c<right[0]:
      heappush(right,c)
    elif right[0]<=c:
      heappush(right,c)
  print(mid)
