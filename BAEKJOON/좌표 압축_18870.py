import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


def binarySearch(targ, arr, l):
	left = 0
	right = l - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < targ:
			left = mid + 1
		elif arr[mid] == targ:
			return mid
		else:
			right = mid - 1
	return -1
	
	
def solve(xs, N):
	xsSort = sorted(xs)
	xsSortDelDup = [xsSort[0]]
	l = 1
	for i in range(1, N):
		if xsSort[i] != xsSort[i-1]:
			xsSortDelDup.append(xsSort[i])
			l += 1
	ans = []
	for n in range(N):
		ans.append(binarySearch(xs[n], xsSortDelDup, l))
	
	print(*ans)
	
	
if __name__ == "__main__":
	N = int(In())
	xs = [*MIS()]
	solve(xs, N)