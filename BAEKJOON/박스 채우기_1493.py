#(python3/pypy) 직관적인 재귀 분할정복 풀이로는 메모리초과/시간초과 발생하는 문제
import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
l,w,h=MIS()
C=int(In())
cubes=[] #i가 증가하는 순으로 주어짐 - [제곱수,개수]
for i in range(C):
  a,b=MIS()
  cubes.append([1<<a, b])
V=l*w*h
mnn=min(l,w,h)

bf=0
ans=0
used=[0]*(C+1)
for i in range(C-1, -1, -1):
  cnt=0 #현재 큐브가 채울 수 있는 최대 개수
  cl=cubes[i][0]
  cv=cl*cl*cl
  #이전 큐브들로 채웠던 박스는 다음 큐브를 8배 더 사용해서 채워야 하기 때문에 *8
  bf*=8
  if mnn >= cl:
    #분할은 단순 나누기가 아니라 shift 개념
    #빈 박스에 현재 큐브로 새로 쌓고 이전에 쌓았던 큐브 개수를 차감하는 방식
    #누적합 개념 살짝 들어감
    cnt=min((l >> i) * (w >> i) * (h >> i)-bf,cubes[i][1])
    used[i]=cnt
    bf+=used[i]
    ans+=used[i]

if bf==l*w*h: #큐브의 개수 확인
  print(ans)
else:
  print(-1)