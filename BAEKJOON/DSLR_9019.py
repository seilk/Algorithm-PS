#str은 많이 무거우므로 사용을 최소화 하는것이 시간적으로 도움이 됨
#길이가 긴 str을 계속 들고 다니는 것은 시간적으로 비효율적임
#딕셔너리는 key가 str이면 효율이 좋지 않을 수 있음
#해당 번호를 어떻게 만들었는지 기록하고 역추적으로 str을 합침
import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
D = lambda n : (2*n)%10000
S = lambda n : 9999 if n == 0 else n-1
L = lambda n : (n//1000+(n%1000)*10)# 1234->2341->3412, 123->1230 #rotate는 str사용하고 시간복잡도도 크기 때문에 비추
R = lambda n : (n//10+(n%10)*1000)

def BFS(st:int, target:int):
  dq=deque([st])
  visiteds[st]=1
  while dq:
    num=dq.popleft()
    for nnum,nl in [(D(num),"D"),(S(num),"S"),(L(num),"L"),(R(num),"R")]:
      if visiteds[nnum]=="":
        if nl=="D" and 2*num>=10000: #D
          visiteds[nnum]="D1"
          if nnum==target:
            return
          dq.append(nnum)
        elif nl=="D" and 2*num<=9999:
          visiteds[nnum]="D2"
          if nnum==target:
            return
          dq.append(nnum)
        else: # S L R
          visiteds[nnum]=nl
          if nnum==target:
            return
          dq.append(nnum)

def find(x,y):
  dqq=deque([])
  ans=y
  while ans!=x:
    if visiteds[ans]=="D1":
      dqq.appendleft("D")
      ans=(ans+10000)//2 # 곱의 나머지 거꾸로 연산
    elif visiteds[ans]=="D2":
      dqq.appendleft("D")
      ans//=2
    elif visiteds[ans]=="S" and ans!=9999:
      dqq.appendleft("S")
      ans+=1
    elif visiteds[ans]=="S" and ans==9999:
      dqq.appendleft("S")
      ans=0
    elif visiteds[ans]=="R":
      dqq.appendleft("R")
      ans=L(ans)
    elif visiteds[ans]=="L":
      dqq.appendleft("L")
      ans=R(ans)
  print(*dqq,sep="") #스트링을 출력하는것보다 deque+asterisk 출력이 효율 더 좋음
  return


if __name__=="__main__":
  T = int(In())
  for i in range(T):
    visiteds=[""]*10001
    x,y=MIS()
    BFS(x,y)
    find(x,y)