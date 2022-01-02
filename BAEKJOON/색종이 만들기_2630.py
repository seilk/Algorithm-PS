import sys
input = sys.stdin.readline
l = int(input().rstrip())
arr = [input().rstrip().split() for i in range(l)]
blue = 0
white = 0


def DivideConquer(arr):
  global blue, white
  ll = len(arr)
  clr = arr[0][0]
  same = True
  if ll == 1:
    if clr == "1":
      blue += 1
    elif clr == "0":
      white += 1
    return
  for i in range(ll):
    for j in range(ll):
      if clr != arr[i][j]:
        same = False
        break
    if not same:
      break

  if not same:
    nl = int(ll/2)
    DivideConquer([i[:nl] for i in arr[:nl]])
    DivideConquer([i[nl:] for i in arr[:nl]])
    DivideConquer([i[:nl] for i in arr[nl:]])
    DivideConquer([i[nl:] for i in arr[nl:]])
  else:
    if clr == "1":
      blue += 1
    elif clr == "0":
      white += 1


DivideConquer(arr)


print(white)
print(blue)
