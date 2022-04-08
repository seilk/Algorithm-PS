import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

n, k = MIS()
ipt = [*MIS()]
check = [0] * (100_001)
left = 0
right = 0
ans = 0
while left <= right:
	ans = max(right - left, ans)
	if right == n:
		left += 1
		continue
	if check[ipt[right]] < k :
		check[ipt[right]] += 1
		right += 1
	else:
		check[ipt[left]] -= 1
		left += 1


print(ans)
