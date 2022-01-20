import sys

input = sys.stdin.readline
N = int(input().rstrip())
video = [list(input().rstrip()) for i in range(N)]


def divideconq(x, y, N):
  color = video[x][y]
  SAME = True
  for xx in range(x, x + N):
    for yy in range(y, y + N):
      if video[xx][yy] != color:
        SAME = False
        break
    if not SAME:
      break
  if SAME:
    return str(color)
  return "(" + divideconq(x, y, N // 2) \
         + divideconq(x, y + (N // 2), N // 2) \
         + divideconq(x + (N // 2), y, N // 2) \
         + divideconq(x + (N // 2), y + (N // 2), N // 2) + ")"


print(divideconq(0, 0, N))
