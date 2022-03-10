def solution(triangle):
	height = len(triangle)
	dp = [[] for i in range(height)]
	dp[0].append(0)
	dp[0].append(triangle[0][0])
	dp[1].append(dp[0][1] + triangle[1][0])
	dp[1].append(dp[0][1] + triangle[1][1])
	w = 3
	for h in range(2, height):
		for i in range(w):
			if i == 0:
				dp[h].append(triangle[h][0] + dp[h-1][0])
			elif i == w-1:
				dp[h].append(triangle[h][i]+dp[h-1][i-1])
			else:
				dp[h].append(max(triangle[h][i] + dp[h-1][i-1], triangle[h][i] + dp[h-1][i]))
		w += 1
	print(max(dp[height-1]))
	return
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])