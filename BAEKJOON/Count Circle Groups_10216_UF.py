import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def find(x, arr):
	if arr[x] != x:
		arr[x] = find(arr[x], arr)
	return arr[x]


def union(x, y, arr):
	a = find(x, arr)
	b = find(y, arr)
	if a < b:
		arr[b] = arr[a]
	else:
		arr[a] = arr[b]


def dist(x1, y1, x2, y2):
	return (x1 - x2) ** 2 + (y1 - y2) ** 2


def solve():
	N = int(In())
	xx = [0] * N
	yy = [0] * N
	rr = [0] * N
	
	for n in range(N):
		xx[n], yy[n], rr[n] = MIS()
	
	arr = [i for i in range(N)]
	# ans = 0
	for n in range(N):
		for m in range(n + 1, N): # 조합이므로 (a,b)==(b,a)
			# math 라이브러리 사용하면 시간초과. 두 점 사이 거리 구할 때 sqrt 사용 자제
			if dist(xx[n], yy[n], xx[m], yy[m]) <= (rr[n] + rr[m]) ** 2:
				if find(n, arr) == find(m, arr): continue # 부모 노드가 같으면 continue
				union(n, m, arr)
				
	tot = 0 # 부모노드 개수 갱신
	vist = [0] * N
	for n in range(N):
		# arr의 값으로 찾으면 안됨, arr의 값의 find로 찾아야함, 아직 부모노드가 갱신이 안된 지점이 있을 수 있음.
		if vist[find(arr[n], arr)] == 0:
			vist[arr[n]] = 1
			tot += 1
	print(tot) # 이렇게 해주는 방법도 있고 union 해줄때 마다 흡수되는 노드의 개수를 1개씩 카운트해줘서 (전체 노드 - 흡수된 노드)의 방법도 있음.

if __name__ == "__main__":
	T = int(In())
	for t in range(T):
		solve()
