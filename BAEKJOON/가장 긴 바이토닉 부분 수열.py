import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def L_I_S(arr, N):
	dp = [1] * N
	for i in range(N):
		for j in range(i):
			if arr[j] < arr[i]:
				dp[i] = max(dp[i], dp[j] + 1)
	return dp

N = int(In())
arrForward = [*MIS()]
arrBackward = arrForward[::-1]
dpForward = L_I_S(arrForward, N)
dpBackward = L_I_S(arrBackward, N)[::-1]; #뒤집어 준다
mxx = 1
for i in range(N):
	mxx = max(mxx, dpBackward[i] + dpForward[i] - 1)
print(mxx)