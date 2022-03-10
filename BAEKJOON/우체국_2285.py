import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
town = []
for n in range(1, N+1):
	x, y = MIS() # 마을 좌표, 사람 수
	town.append((x, y))
town.sort() # 마을 좌표 순으로 정렬
townPrefix = [0] * N
townPrefix[0] = town[0][1]

for i in range(1, N):
	townPrefix[i] = townPrefix[i-1]+town[i][1]
	
left = 0
right = N - 1
ans = 100_001
while left <= right:
	mid = (left + right) // 2
	leftPeoples = townPrefix[mid]
	rightPeoples = townPrefix[N-1] - townPrefix[mid]
	if leftPeoples < rightPeoples:
		left = mid + 1
	else: # 좌우 균형이 같거나 왼쪽이 더 큰 경우
		# 좌표를 감소시키는 경우에 ans를 저장한다. (마을의 최소 좌표 리턴 -> 좌표상으로 왼쪽에 있어야함)
		# 거리가 같은 경우에도 right를 더 줄여보면서 좌표가 더 작은 마을이 있는지 확인한다.
		right = mid - 1
		ans = min(ans, town[mid][0])
	
print(ans)