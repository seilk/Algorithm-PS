import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def floyd(n):
	for k in range(1, n + 1):
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				if arr[i][k] == True and arr[k][j] == True:
					arr[i][j] = True

n, k = MIS()
arr = [[0] * (n+1) for i in range(n + 1)]
for i in range(1, n + 1):
	arr[i][i] = 1
	
dp = [[0] * (n + 1) for i in range(n + 1)]
for _ in range(k):
	front, back = MIS()
	arr[front][back] = 1
	
floyd(n)

g = int(In())
for _ in range(g):
	u, v = MIS()
	if arr[u][v] == True:
		print(-1)
	elif arr[v][u] == True:
		print(1)
	else:
		print(0)
	

	
	