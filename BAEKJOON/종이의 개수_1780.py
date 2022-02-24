import sys
input = sys.stdin.readline
l = int(input().rstrip())
arr = [input().rstrip().split() for i in range(l)]
minus = 0
zero = 0
plus = 0

def DivideConquer(arr):
  global minus, zero, plus
  ll = len(arr)
  clr = arr[0][0]
  same = True
  if ll == 1:
    if clr == "-1":
      minus += 1
    elif clr == "0":
      zero += 1
    elif clr == "1":
      plus += 1
    return

  for i in range(ll):
    for j in range(ll):
      if clr != arr[i][j]:
        same = False
        break
    if not same:
      break

  if not same:
    a = int(ll/3)
    b = int((ll/3)*2)
    DivideConquer([i[:a] for i in arr[:a]])
    DivideConquer([i[a:b] for i in arr[:a]])
    DivideConquer([i[b:] for i in arr[:a]])
    DivideConquer([i[:a] for i in arr[a:b]])
    DivideConquer([i[a:b] for i in arr[a:b]])
    DivideConquer([i[b:] for i in arr[a:b]])
    DivideConquer([i[:a] for i in arr[b:]])
    DivideConquer([i[a:b] for i in arr[b:]])
    DivideConquer([i[b:] for i in arr[b:]])
  else:
    if clr == "-1":
      minus += 1
    elif clr == "0":
      zero += 1
    elif clr == "1":
      plus += 1


DivideConquer(arr)


print(minus)
print(zero)
print(plus)
