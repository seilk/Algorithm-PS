import sys
from bisect import bisect_left, bisect_right
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


def init():
	target = int(In())
	N = int(In())
	arr1 = [*MIS()]
	M = int(In())
	arr2 = [*MIS()]
	pf1 = [0, arr1[0]]
	for i in range(2, N+1) : pf1.append(pf1[i-1] + arr1[i-1])
	pf2 = [0, arr2[0]]
	for i in range(2, M+1) : pf2.append(pf2[i-1] + arr2[i-1])
	return target, N, M, pf1, pf2



def makeTeam(pf1, pf2):
	team1 = []
	team2 = []
	for i in range(N + 1):
		for j in range(i):
			team1.append(pf1[i] - pf1[j])
			
	for i in range(M + 1):
		for j in range(i):
			team2.append(pf2[i] - pf2[j])
	team1.sort()
	team2.sort()
	return team1, team2

T, N, M, pf1, pf2 = init()
team1, team2 = makeTeam(pf1, pf2)
l1, l2 = len(team1), len(team2)
"""
1 4 5 7 pa[i] - pa[j] (i > j)
1 4 6 pb[k] - pb[l] (k > l)

pa[i] - pa[j] + pb[i] - pb[j] = T
N^2*M^2 -> N^3logM -> N^2 * logM^2
"""
ans = 0
for i in range(l1):
	s1 = team1[i]
	left = 0
	right = l2 - 1
	ans += bisect_right(team2, T - s1) - bisect_left(team2, T - s1)
	"""어떤 구간에 해당 숫자가 몇개 있는지 확인"""

print(ans)