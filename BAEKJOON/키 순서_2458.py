import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def floyd(n, upTall, downTall) :
	for k in range(1, n+1) :
		for i in range(1, n+1) :
			for j in range(1, n+1) :
				if grp[i][j] == 1 : continue
				if grp[ i ][ k ] == 1 and grp[ k ][ j ] == 1 :
					grp[ i ][ j ] = 1
					upTall[ i ] += 1
					downTall[ j ] += 1
	return [ i+j for i, j in zip(upTall, downTall) ]

n, m = MIS()
grp = [ [ 0 ]*501 for i in range(501) ]
upTall = [ 0 ]*(n+1)
downTall = [ 0 ]*(n+1)
for _ in range(m) :
	u, v = MIS()
	grp[ u ][ v ] = 1
	upTall[ u ] += 1
	downTall[ v ] += 1

ansList = floyd(n, upTall, downTall)
ans = 0
for i in range(1, n+1) :
	if ansList[ i ] == n-1 :
		ans += 1
print(ans)
