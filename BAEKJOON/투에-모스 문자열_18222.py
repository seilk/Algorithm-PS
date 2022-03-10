import sys
from math import *
In = lambda : sys.stdin.readline().rstrip()

def rec(kk, k, sig):
	if kk == 1:
		if sig & 1 : return 1
		else : return 0
	if k <= kk//2:
		return rec(kk//2, k, sig)
	
	else:
		return rec(kk//2, k - (kk//2), sig + 1)

k = int(In())
kk = 2 ** (ceil(log2(k)))
print(rec(kk,k, 0))
