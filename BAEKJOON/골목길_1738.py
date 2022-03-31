import sys
from collections import deque

In = lambda:sys.stdin.readline().rstrip()
MIS = lambda:map(int,In().split())


def b_f(N,nodesWithEnd,start=1):
	INF = 1e9
	parent = [ i for i in range(N+1) ]  # 부모 노드 저장
	dist = [ INF ]*(N+1)
	dist[ start ] = 0

	for _ in range(N-1):  #1
		for i in range(1,N+1):
			for nxt,dd in grp[ i ]:
				if dist[ i ]==INF: continue
				if i!=1 and nxt==1: continue
				if dist[ nxt ] > dist[ i ]+dd:
					parent[ nxt ] = i
					dist[ nxt ] = dist[ i ]+dd

	for i in range(1,N+1):  #check cycle
		for nxt,dd in grp[ i ]:
			if dist[ i ]==INF: continue
			if dist[ nxt ] > dist[ i ]+dd:
				if nodesWithEnd[ nxt ]==1: return [ -1 ]

	if dist[ N ] >= INF: return [ -1 ]
	cur = N
	ans = deque([ N ])
	while cur!=1: # 경로 역추적
		ans.appendleft(parent[ cur ])
		cur = parent[ cur ]
	return ans


def findNodeWithEnd(N): # End 지점과 연결된 노드들 체크
	vist = [ 0 ]*(N+1)
	dq = deque([ N ])
	while dq:
		cur = dq.popleft()
		for nxt,d in grpReversed[ cur ]:
			if vist[ nxt ]==1: continue
			vist[ nxt ] = 1
			dq.append(nxt)
	return vist


def init():
	N,M = MIS()
	grp = [ [ ] for i in range(N+1) ]
	grpReversed = [ [ ] for i in range(N+1) ]

	for m in range(M):
		u,v,d = MIS()
		grp[ u ].append([ v,-d ])
		grpReversed[ v ].append([ u,-d ]) # findNodeWithEnd를 위한 추가 리스트
	return N,M,grp,grpReversed


N,M,grp,grpReversed = init()
nodesWithEnd = findNodeWithEnd(N)
print(*b_f(N,nodesWithEnd))
