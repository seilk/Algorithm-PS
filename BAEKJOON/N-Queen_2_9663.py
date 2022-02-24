import sys


def CHECK(r, Nq):
  # 각 행마다 퀸은 한개만 존재할 수 있다
  # 각 행을 +1 해주면서 해당 행에 어느 열에 퀸이 존재할 수 있는지 확인
  # visitRow[idx] = val : idx행에 들어가는 Queen은 val열에 존재
  global cnt
  if Nq == N:
    cnt += 1
    return
  for c in range(N):  # 열 선택기 (1~N)
    FLG = True  # 대각성분 확인 FLAG
    if visitCol[c] == -1:  # 아직 선택되지 않은 열을 골라야 함
      for i in range(0, r + 1):  # 행 선택기 : r까지의 행을 모두 확인해서 기울기 확인
        if abs(r + 1 - i) == abs(c - visitRow[i]): # 기울기 확인
          FLG = False
          break
      if FLG:
        visitRow[r + 1], visitCol[c] = c, 1
        CHECK(r + 1, Nq + 1)
        visitRow[r + 1], visitCol[c] = -1, -1


if __name__ == "__main__":
  R = lambda: sys.stdin.readline().rstrip()
  N = int(R())
  cnt = 0
  visitRow = [-1] * N  # 해당 인덱스 row에 column의 위치 저장
  visitCol = [-1] * N  # 해당 인덱스의 col이 선택됐는지 여부
  CHECK(-1, 0)
  print(cnt)
