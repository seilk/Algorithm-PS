import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def floyd(n) :
	INF = float("inf")
	saveAnswer = [ [ INF ]*(n+1) for i in range(n+1) ]
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if grp[i][j] == -1 : continue
			saveAnswer[i][j] = grp[i][j]
	for k in range(1, n+1) :
		for i in range(1, n+1) :
			for j in range(1, n+1) :
				'''양방향으로 갈 수 있으면 최대한 양방향으로 가야하므로 값을 지정해서 최솟값을 배정해줘야 함'''
				if saveAnswer[ i ][ j ]>saveAnswer[ i ][ k ]+saveAnswer[ k ][ j ] :
					saveAnswer[ i ][ j ] = saveAnswer[ i ][ k ]+saveAnswer[ k ][ j ]

	return saveAnswer

n, m = MIS()

grp = [ [ -1 ]*(n+1) for i in range(n+1) ]
for i in range(n+1) :  # grp setting
	grp[ i ][ i ] = 0

oneWay = [ [ 0 ]*(n+1) for i in range(n+1) ]
for _ in range(m) :  # make graph
	u, v, b = MIS()
	if b == 0 :
		grp[ u ][ v ] = 0
		grp[ v ][ u ] = 1
	else :
		grp[ u ][ v ] = 0
		grp[ v ][ u ] = 0

saveAnswer = floyd(n)
queries = int(In())
for q in range(queries) :
	s, e = MIS()

	print(saveAnswer[ s ][ e ])
