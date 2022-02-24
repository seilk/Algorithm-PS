# math.ceil 오류.. 실수를 다루는 함수는 최대한 안쓰는거 권장
import sys

N, K = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
v.sort()
ans = float("inf")
for i in range(1, len(v)):
  velocity = v[i] * (len(v) - i) + v[0] * i
  if K % velocity==0:
    x = K//velocity
  else :
    x = (K // velocity + 1)
  ans=min(ans,x)
print(ans)