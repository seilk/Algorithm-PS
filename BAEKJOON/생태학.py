import sys
from collections import defaultdict

# f = open("sth.txt")
lst = []
while 1:
	tree = sys.stdin.readline().rstrip()
	if not tree:
		break
	lst.append(tree)

dix = defaultdict(int)
for tree in lst :
	tree = tree.replace("\n", "")
	dix[tree] += 1

cnt = len(lst)

ans = []
for key, val in dix.items():
	dix[key] = round((val/cnt) * 100, 4)
	ans.append([key, dix[key]])

ans.sort()
for i in ans:
	print("{} {:.4f}".format(i[0], i[1]))