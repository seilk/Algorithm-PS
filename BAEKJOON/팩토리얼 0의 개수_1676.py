import sys
from math import log
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
log5 = lambda x: int(log(x,5))
# 1~N까지 수에서 5의 배수의 개수를 추출하면됨
N=int(In())
ANS=0
while N>0:
  ANS+=N//5
  N//=5
print(ANS)