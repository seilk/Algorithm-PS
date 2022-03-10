import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
li = [*MIS()]
li.sort()
liSub = []
for i in range(N):
	for j in range(i+1, N):
		if i == j: continue
		liSub.append((i, j))

ans = [-1e9,-1,-1]
for u, v in liSub:
	liTmp = li[:u] + li[u+1:v] + li[v+1:]
	left = 0
	right = N-3
	while left <= right:
		mid = (left + right) // 2
		if li[u] + li[v] + liTmp[mid] > 0:
			right = mid - 1
		elif li[u] + li[v] + li[mid] == 0:
			print(*sorted([li[u],li[v],liTmp[mid]]))
			sys.exit(0)
		else:
			left = mid + 1
	if abs(li[u] + li[v] + liTmp[left]) < abs(li[u] + li[v] + liTmp[right]):
		tmp = [li[u], li[v], liTmp[left]]
	else:
		tmp = [li[u], li[v], liTmp[right]]
	if abs(sum(ans)) > abs(sum(tmp)):
		ans = [tmp[0], tmp[1], tmp[2]]
print(*sorted(ans))
