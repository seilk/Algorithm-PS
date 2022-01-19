import sys

input = sys.stdin.readline
S = int(input().rstrip())
START = 1
END = 4_294_967_295
complete = False
while START <= END:
  MID = (START + END) // 2
  SUM = 0
  for i in range(1, MID + 1): #1부터 순서대로 덧셈
    SUM += i
    if SUM > S:
      break
  if i < MID or SUM > S: # MID의 크기가 크다고 판단
    END = MID - 1
  elif SUM == S:
    print(MID)
    complete = True
    break
  else :
    START = MID + 1
if not complete:
  print(END)