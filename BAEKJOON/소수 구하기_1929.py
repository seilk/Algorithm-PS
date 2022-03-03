import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
print = sys.stdout.write
arr = [0] * (M+1)
arr[1] = 1
for i in range(2, M+1):
	for j in range(2, M//i+1): # 자기 자신은 제외하고 배수를 지워줌
		arr[i*j] = 1

for i in range(N, M+1):
	if arr[i] == 0:
		print("%s" % i + "\n")
		