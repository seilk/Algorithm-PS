import sys

In = lambda : sys.stdin.readline().rstrip()

num = [0]+[*map(int, list(In()))]
ans = 0
MOD = 1000000
length = len(num)
dp = [0]*(length)
dp[0] = 1
for i in range(1, length) :
	if num[i] != 0 :  # 숫자가 0이 들어갈 수 있기 때문에 조건 포함시켜야 함
		dp[i] = (dp[i-1]+dp[i])%MOD
	if 10 <= num[i-1]*10+num[i] <= 26 :  # 01, 02, 03 같은 수는 알파벳으로 표현할 수 없음 10부터 가능
		dp[i] = (dp[i]+dp[i-2])%MOD

print(dp[-1]%MOD)
