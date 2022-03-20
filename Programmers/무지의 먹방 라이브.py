from heapq import *


def solution(ft, k):
	new_ft = [(val, idx + 1) for idx, val in enumerate(ft)]  # food_time을 순서와 함께 새로 정의
	heapify(new_ft)  # heap 이진 트리 형태로 갱신
	spendTime = 0
	prev = 0
	l = len(ft)  # 남아있는 음식의 가짓수
	ans = -1  # k초뒤의 방송사고 뒤 음식을 먹는것이 불가능 할 때 == 모든 음식의 합 시간이 k 보다 작을 때
	if sum(ft) > k:
		'''현재까지 걸린 전체 시간 + (현재 가장 빨리 먹을 수 있는 음식의 사이클 - 지금까지 거친 사이클 횟수) * 남은 음식 수 <= k
		(현재 가장 빨리 먹을 수 있는 음식 시간 - 지금까지 거친 사이클 횟수) * 남은 음식 수
		== 현재 가장 빨리 먹을 수 있는 음식은 총 n 사이클이고 그 시간은 n * l 이다.'''
		while spendTime + (new_ft[0][0] - prev) * l <= k:
			time, idx = heappop(new_ft)
			'''처음부터 현재 음식까지 먹는데 걸리는 전체 시간 == 이전까지 걸린 시간 + 현재 음식을 먹는데까지 걸리는 시간'''
			spendTime += (time - prev) * l
			''' prev == 현재 까지 진행된 사이클의 수. 따라서 현재 음식을 다 먹는데 걸리는 사이클은
			(원래 다 먹기까지 걸리는 사이클 - 현재까지 걸린 사이클) 이다. 걸리는 시간(t)은 여기서 전체 음식 수를 곱한다.'''
			l -= 1
			prev = time
		new_ft.sort(key=lambda x: x[1])
		ans = new_ft[(k - spendTime) % l][1]
	return ans


print(solution([3, 1, 2], 5))
