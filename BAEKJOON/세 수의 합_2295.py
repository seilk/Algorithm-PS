import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

if __name__ == "__main__":
	N = int(In())
	arr = [int(In()) for i in range(N)]
	team = []
	for i in range(N):
		for j in range(N):
			team.append(arr[i] + arr[j])
	
	team.sort()
	ans = -1
	for r in range(N):
		for z in range(N):
			if arr[r] - arr[z] <= 0 : continue
			target = arr[r] - arr[z]
			left = 0
			right = N**2
			while left <= right:
				mid = (left + right) // 2
				if team[mid] < target:
					left = mid + 1
				elif team[mid] == target:
					ans = max(ans, arr[r])
					break
				else:
					right = mid - 1
	print(ans)
	
	
			
			