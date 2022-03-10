import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def swap(a, b):
	return b, a


def find(x, arr):
	if arr[x] != x:
		arr[x] = find(arr[x], arr)
	return arr[x]


def union(x, y, arr, p):
	a = find(x, arr)
	b = find(y, arr)
	if a > b:
		a, b = swap(a, b)  # 항상 a를 더 작은 수로 swap
	if a == b:
		return
	p[a] += p[b]
	arr[b] = a


N = int(In())
arr = [i for i in range(1_000_001)]
p = [1] * (1_000_001)  # I를 해주지 않은 로봇의 부품의 쿼리가 요청될 수 있음
ans = []
for _ in range(N):
	info = In().split()
	if info[0] == "I":
		info[1] = int(info[1])
		info[2] = int(info[2])
		union(info[1], info[2], arr, p)
	else:
		info[1] = int(info[1])
		ans.append(p[find(info[1], arr)])

print(*ans, sep="\n")
