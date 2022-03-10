import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


def DFS(i, xx, yy, rr, N):
	global vist
	for j in range(N):
		if not vist[j]:
			if dist(xx[i], yy[i], xx[j], yy[j]) <= (rr[i] + rr[j]) ** 2:
				vist[j] = 1
				DFS(j, xx, yy, rr, N)


def dist(x1, y1, x2, y2):
	return (x1 - x2)**2 + (y1 - y2)**2


def solve():
	global arr, vist
	N = int(In())
	xx = [0] * N
	yy = [0] * N
	rr = [0] * N
	
	for n in range(N):
		xx[n], yy[n], rr[n] = MIS()

	ans = 0
	vist = [0] * N
	for n in range(N):
		if not vist[n]:
			vist[n] = 1
			DFS(n, xx, yy, rr, N)
			ans+=1

	print(ans)
	
if __name__ == "__main__":
	T = int(In())
	for t in range(T):
		solve()