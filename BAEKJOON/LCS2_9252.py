import sys

R = lambda: sys.stdin.readline().rstrip()
X, Y = R(), R()
LX = len(X)
LY = len(Y)
X="-"+X
Y="-"+Y
DP = [[[0, ""] for j in range(LX + 1)] for i in range(LY + 1)]
for y in range(1, LY + 1):
  for x in range(1, LX + 1):
    if Y[y] == X[x]:
      DPSET = [[DP[y-1][x][0],DP[y-1][x][1]],[DP[y][x-1][0],DP[y][x-1][1]],[DP[y-1][x-1][0]+1,DP[y-1][x-1][1]+X[x]]]
      MXX = [-1,""]
      for i in range(3):
        if MXX[0] < DPSET[i][0]:
          MXX[0] = DPSET[i][0]
          MXX[1] = DPSET[i][1]
      DP[y][x][0] = MXX[0]
      DP[y][x][1] = MXX[1]
    else:
      DPSET = [[DP[y-1][x][0],DP[y-1][x][1]],[DP[y][x-1][0],DP[y][x-1][1]],[DP[y-1][x-1][0],DP[y-1][x-1][1]]]
      MXX = [-1,""]
      for i in range(3):
        if MXX[0] < DPSET[i][0]:
          MXX[0] = DPSET[i][0]
          MXX[1] = DPSET[i][1]
      DP[y][x][0] = MXX[0]
      DP[y][x][1] = MXX[1]
if len(DP[LY][LX]) > 1:
  print(*DP[LY][LX], sep="\n")
else:
  print(0)
