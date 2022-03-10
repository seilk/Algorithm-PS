import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
arr = [*MIS()]
arr.sort()

M = int(In())
fi = [*MIS()]

for target in fi:
	left = 0
	right = N - 1
	flg = False
	while left <= right:
		mid = (left + right) // 2
		if target == arr[mid]:
			flg = True
			break
		if target > arr[mid]:
			left = mid + 1
		if target < arr[mid]:
			right = mid - 1
	print(0 if flg == False else 1)