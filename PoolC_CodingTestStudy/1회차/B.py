import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def shuffle(K, arr):
	l = N
	dummy = arr[l-2**K:]
	arr = dummy + arr[:l-2**K]
	level = 2
	ll = 2**K
	while level <= K + 1:
		rem = dummy[:ll-2**(K-level+1)]
		dummy = dummy[ll-2**(K-level+1):]
		arr = dummy + rem + arr[ll:]
		ll = 2**(K-level+1)
		level += 1
	return arr

def search(d, cur, targ, ks):
	if d == 2:
		if cur == targ:
			return ks
		return False
	for k in range(1, N+1):
		res = search(d + 1, shuffle(k, cur), targ, ks + [k])
		if res :
			return res
	
N = int(In())
arr = [*MIS()]
initCards = list(range(1,N+1))
print(*search(0, initCards, arr, []))