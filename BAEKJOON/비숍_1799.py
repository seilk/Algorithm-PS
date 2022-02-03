import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def tryEven():
  global MXX, SUM
  MXX = -1
  SUM = 0
  backTracking(2)
  MXX_even = MXX
  return MXX_even

def tryOdd():
  global MXX, SUM
  MXX = -1
  SUM = 0
  backTracking(1)
  MXX_odd = MXX
  return MXX_odd


def setMatching(): # 대각선으로 좌표를 생각했을때 하나의 대각선과 교차하는 다른 축의 대각선의 좌표 매칭
  matching = [[] for i in range(2 * N)]
  for n in range(1, N + 1):
    matching[n].append(N - n + 1)
    for _ in range(1, n):
      matching[n].append(matching[n][-1] + 2)
  return matching

def backTracking(d):
  global v_71, v_511, MXX, SUM, matching
  MXX = max(MXX, SUM)
  for cur in range(d,2*N,2): # 홀수, 짝수를 구분하기 때문에 range gap=2
    if not v_71[cur]:
      # N을 넘어서는 cur에 대해서는 대칭되는 수의 정보 사용
      ccur = 2*N-cur if cur > N else cur
      cur_r = 0 if cur <= N else cur-N
      cur_c = cur-1 if cur <= N else N-1
      # 기준으로 잡은 대각선과 교차되는 대각선은 cur개 있음
      for i in range(ccur):
        # 좌표는 행++ 열-- 방향으로 진행 (왼쪽으로 90도 기울여서 보면 위->아래 방향임)
        new_r, new_c = cur_r+i, cur_c-i
        # 비숍이 들어갈 수 있는 조건 확인 - 좌표의 범위, 장애물 유무, 교차되는 대각선의 비숍 유무
        if 0<=new_r<N and 0<=new_c<N and BOARD[new_r][new_c]==1:
          # 교차되는 i번째 대각선상에 비숍이 존재하면 기준으로 잡은 대각선에서 i번째 위치에는 비숍을 두지 못한다.
          if not v_511[matching[ccur][i]]:
            v_71[cur],v_511[matching[ccur][i]]=1,1
            SUM+=1
            backTracking(cur + 2)
            SUM-=1
            v_71[cur],v_511[matching[ccur][i]]=0,0


def solve(): # 좌표를 90도 회전시켜 하나의 대각선에는 비숍이 하나만 존재한다는 조건을 사용한다.
  global v_71, v_511, MXX, SUM, matching
  matching = setMatching()
  v_71 = [0]*(2*N) # 7시에서 1시방향으로 뻗어나가는 대각선에 대한 좌표
  v_511 = [0]*(2*N) # 5시에서 11시방향으로 뻗어나가는 대각선에 대한 좌표
  print(tryOdd()+tryEven()) # 홀수 부분과 짝수 부분은 서로 간섭하지 않기 때문에 각각 계산해줌, 같이 계산했을 때에는 TLE 발생


if __name__ == "__main__":
  N=int(In())
  BOARD=[[*MIS()] for i in range(N)]
  solve()