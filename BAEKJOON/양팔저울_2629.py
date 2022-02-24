import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
print = lambda x : sys.stdout.write(x)

def recursion(i, w):
  if i>C or dpw[i][w]:
    return
  dpw[i][w]=True
  recursion(i+1, abs(w-weight[i])) # 구슬과 같은 접시에 놓는 경우
  recursion(i+1, w) # 안놓는 경우
  recursion(i+1, w+weight[i]) # 구슬 반대편 접시에 놓는 경우

if __name__=="__main__":
  C=int(In())
  weight=[*MIS()]+[0]
  B=int(In())
  ball=[*MIS()]
  dpw=[[False for j in range(40001)] for i in range(C+1)]
  recursion(0,0)
  for b in ball:
    if dpw[C][b]:
      print("Y ")
    else:
      print("N ")
