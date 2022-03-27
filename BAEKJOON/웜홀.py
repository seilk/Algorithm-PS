import sys

In = lambda:sys.stdin.readline().rstrip()
MIS = lambda:map(int,In().split())


def b_f(n,start=1):
	INF = float("inf")
	dist = [ 1e9 ]*(n+1)
	dist[ start ] = 0
	for i in range(n-1):
		for j in range(1,n+1):
			for nxt,d in grp[ j ]:
				if dist[ nxt ] > dist[ j ]+d:
					dist[ nxt ] = dist[ j ]+d

	for i in range(1,n+1):
		for nxt,d in grp[ i ]:
			if dist[ nxt ] > dist[ i ]+d:
				return "YES"
	return "NO"


T = int(In())
for t in range(T):
	n,m,w = MIS()
	grp = [ [ ] for i in range(n+1) ]
	for _ in range(m):
		u,v,d = MIS()
		grp[ u ].append([ v,d ])
		grp[ v ].append([ u,d ])
	for _ in range(w):
		u,v,d = MIS()
		grp[ u ].append([ v,-d ])
	print(b_f(n))
