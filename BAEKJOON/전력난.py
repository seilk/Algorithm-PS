import sys
from heapq import *

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def swap(a, b) :
	return b, a

def find(p) :
	if parent[p] != p :
		parent[p] = find(parent[p])
	return parent[p]

def union(u, v) :
	a = find(u)
	b = find(v)
	if a == b : return
	if a > b :
		a, b = swap(a, b)
	parent[b] = a

while 1 :
	num_v, num_e = MIS()
	if num_v == 0 and num_e == 0 :
		break
	parent = [i for i in range(num_v)]
	origin_price = 0
	hq = []
	for _ in range(num_e) :
		u, v, w = MIS()
		origin_price += w
		heappush(hq, (w, u, v))

	minimum_price = 0
	while hq :
		weight, u, v = heappop(hq)
		p_u = find(u)
		p_v = find(v)
		if p_u != p_v :
			union(p_u, p_v)
			minimum_price += weight

	ans = origin_price-minimum_price
	print(ans)
