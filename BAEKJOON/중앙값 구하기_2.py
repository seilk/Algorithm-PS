import sys
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

t = int(In())
for _ in range(t):
	arrSize = int(In())
	arr = [None]
	for i in range(arrSize // 10 + 1):
		for j in [*MIS()]:
			arr.append(j)
	rightMinHeap = []
	leftMaxHeap = []
	mid = -987654321
	ret = []
	for i in range(1, arrSize + 1):
		if i & 1 :
			if not rightMinHeap:
				mid = arr[i]
			elif  arr[i] >= rightMinHeap[0] :
				heappush(rightMinHeap,arr[i])
				mid = heappop(rightMinHeap)
			elif -leftMaxHeap[0] < arr[i] < rightMinHeap[0] :
				mid = arr[i]
			else:
				heappush(leftMaxHeap, -arr[i])
				mid = -heappop(leftMaxHeap)
			ret.append(mid)


		else:
			if not rightMinHeap:
				if arr[i] >= mid:
					heappush(rightMinHeap, arr[i])
					heappush(leftMaxHeap, -mid)
					continue
			if not leftMaxHeap:
				if arr[i] < mid:
					heappush(leftMaxHeap, -arr[i])
					heappush(rightMinHeap, mid)
					continue
			if arr[i] >= rightMinHeap[0]:
				heappush(rightMinHeap, arr[i])
				heappush(leftMaxHeap, -mid)

			elif mid <= arr[i] < rightMinHeap[0]:
				heappush(leftMaxHeap, -mid)
				heappush(rightMinHeap, arr[i])
			else:
				heappush(leftMaxHeap, -arr[i])
				heappush(rightMinHeap, mid)

	print(arrSize//2+1)
	length = len(ret)
	if length <= 10:
		print(*ret)
	else:
		for k in range(1, length // 10 + 2):
			if k == length // 10 + 1:
				print(*ret[(k-1)*10:])
				continue
			if k == 1 :
				print(*ret[:k*10])
				continue
			print(*ret[(k-1)*10:k*10])

