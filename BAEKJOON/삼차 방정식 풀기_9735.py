import sys
from math import sqrt, pow
def findDiv(N):
  divs=set()
  n = int(sqrt(abs(N)))
  for i in range(1,n+1):
    if N%i==0:
      divs|={i,-i,N//i,-N//i}
  return divs
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N = int(In())
ans=set()


def calculate(A,B,C,D,n):
  return A * n * n * n + B * n * n + C * n + D

def calAssembly(A,B,C,D,n):
  Ap=A;Bp=B+n*A;Cp=C+n*(Bp);
  return Ap, Bp, Cp

def calRootFomula(A,B,C):
  p = [-1,1]
  ans = set()
  for i in range(2):
    try:
      ans.add((1/(2*A))*(-B+(p[i])*sqrt(B**2-4*A*C)))
    except:
      continue
  return ans

for _ in range(N):
  A,B,C,D=MIS()
  ans=set()
  if D!=0:
    divs = findDiv(D)
    for n in divs:
      if calculate(A,B,C,D,n) == 0:
        ans.add(n)
        Ap,Bp,Cp=calAssembly(A,B,C,D,n)
        ans |= calRootFomula(Ap,Bp,Cp)
  else:
    ans.add(0)
    ans |= calRootFomula(A,B,C)
  print(*sorted(list(ans)))