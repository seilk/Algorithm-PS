import sys
from math import log2
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def shift(v,c,k): # 시간초과
  t=0
  while (1<<t)<k:
    if k - (1<<t) > 0:
      bag.append((v*(1<<t),c*(1<<t)))
    k-=(1<<t)
    t+=1
  bag.append((v*k,c*k))
  return

"""
def shift(v,c,k):
  # 11 = 6 + 3 + 1 + 1, 
  # 13 = 7 + 3 + 2 + 1, 
  # 1~k까지 표현 가능한 수를 k보다 더 작은 값으로 쪼개서 사용
  global bag
  while k>0:
    num=k-(k>>1)
    bag.append((v*num, c*num)) #
    k>>=1
  return
"""

if __name__ == "__main__":
  N,M = MIS()
  bag=[]
  for n in range(N):
    v,c,k=MIS() #무게, 만족도, 개수
    shift(v,c,k)

  dp=[0]*10001
  for i in range(len(bag)): # 물건을 선택하는 중요하지 않음, 중복도 중복대로 처리
    wt=bag[i][0]
    val=bag[i][1]
    for j in range(M,wt-1,-1): # 뒤에서 부터 탐색
      dp[j]=max(dp[j], dp[j-wt]+val) # 현재 물건을 넣어주는 경우 vs 넣어주지 않는 경우
  print(dp[M])

# 2 11
# 1 1 11
# 2 2 13