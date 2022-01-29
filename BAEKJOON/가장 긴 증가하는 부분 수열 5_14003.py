import sys
from collections import deque
from bisect import bisect_left
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N = int(In())
arr = [*MIS()]
L = []
P = [-1]*N
tot=0
for i in range(N):
  if not L:
    L.append(arr[i])
    cur=1
    tot+=1
  elif L[-1] < arr[i]:
    L.append(arr[i])
    tot+=1
    cur=tot
  else:
    # 현재 보고있는 arr의 값이 삽입될 수 있는 가장 작은 인덱스
    # bisect_left는 배열의 오름차순을 기본 정렬로 한다.
    # arr[i]가 삽입되는 위치는 배열의 오름차순을 해치지 않는 선에서 정해진다.
    idx = bisect_left(L, arr[i])
    L[idx] = arr[i]
    cur=idx+1
  # P[i]에는 arr[i]가 L의 몇번째로 삽입되었는지에 대한 정보가 저장된다.
  P[i] = cur

# L의 전체 길이가 LIS의 길이
# L안의 값들은 무작위 값들
LIS_length = tot
ANS=deque([])
for p in range(N-1,-1,-1):
  if P[p] == tot:
    ANS.appendleft(arr[p])
    tot-=1

ANS=list(ANS)
print(LIS_length)
print(*ANS)
