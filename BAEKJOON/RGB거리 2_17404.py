import sys
R = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, R().split())
N = int(R())
INF = float("inf")
TOWN = [list(MIS()) for i in range(N)]
dpTABLE = [[INF, INF, INF] for i in range(N)]
ANS = INF
# 처음집과 마지막집이 연결되어있는게 문제
for a in range(3): # 0번째 집의 색깔을 고정
  dpTABLE[0][a] = TOWN[0][a]
  for i in range(1, N): # 1번째 집부터 N-1번째 집까지 일반적인 RGB거리 처럼 최소값 구해줌
    dpTABLE[i][0] = min(dpTABLE[i-1][1], dpTABLE[i-1][2]) + TOWN[i][0]
    dpTABLE[i][1] = min(dpTABLE[i-1][0], dpTABLE[i-1][2]) + TOWN[i][1]
    dpTABLE[i][2] = min(dpTABLE[i-1][0], dpTABLE[i-1][1]) + TOWN[i][2]
  for j in range(3): # 마지막 집의 최소값을 정할 때 고정시킨 첫번째 집의 색깔과 다른 색깔의 최소값 확인
    if a != j:
      ANS = min(ANS, dpTABLE[N-1][j]) # 세가지 색깔중 하나인데 첫번째 집의 색깔은 제외됨
  dpTABLE[0][a] = INF # 0번째 집 색깔 초기화
print(ANS)