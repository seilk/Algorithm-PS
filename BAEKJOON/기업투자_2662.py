import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
if __name__=="__main__":
  N,M=MIS()
  dp=[[0]*(M+1) for j in range(N+1)] #dp[i][j] = i만원을 1~j기업에 투자했을때 얻을 수 있는 최대이익
  dpc=[[0]*(M+1) for j in range(N+1)]
  arr=[[0]*(M+1) for i in range(N+1)]
for i in range(N):
  tmp=[*MIS()]
  for t in range(1,M+1):
    arr[tmp[0]][t]=tmp[t]
for i in range(1,N+1): #i만원
  for j in range(1,M+1): #j기업
    for k in range(0,i+1): #i=i-k+k, k=0 부터 시작해서 j기업에 아예 투자를 안하는 경우도 생각
      p = dp[i-k][j-1] + arr[k][j] #j기업에 k만원 투자할때의 가치
      if p > dp[i][j]:
        dp[i][j]=p
        dpc[i][j]=k
MXX = dp[N][M] # N만원을 1~M 기업중에서 투자할때 가장 큰 가치
company = [0]*(M+1)
for i in range(M,0,-1):
  if N==0:
    continue
  company[i] = dpc[N][i]
  N-=dpc[N][i]
print(MXX)
print(*company[1:])