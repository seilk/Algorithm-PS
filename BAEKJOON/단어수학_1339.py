import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
wordTerms = []
dix = defaultdict(int)
vist = [0]*10
ans = 0
for i in range(n) :
	lst = list(sys.stdin.readline().rstrip())
	l = len(lst)
	for j in range(l-1, -1, -1):
		dix[lst[l-1-j]] += 10**j

ret = sorted(list(dix.items()), key = lambda x : x[1], reverse=True)
num = 9
ans = 0
for key, val in ret:
	ans += num*val
	num -= 1
	
print(ans)
