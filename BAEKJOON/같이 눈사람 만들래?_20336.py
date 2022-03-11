import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
arr = [*MIS()]
arr.sort()
p = 1e9
for i in range(N-3):
	for j in range(N-1, i+2, -1):
		for k in range(i+1, j):
			x = arr[i] + arr[j]
			left = k+1
			right = j-1
			while left <= right:
				mid = (left + right) // 2
				
				p = min(p, abs(x - (arr[mid] + arr[k])))
				if x - (arr[mid] + arr[k]) > 0:
					left = mid + 1
				else:
					right = mid - 1
print(p)
