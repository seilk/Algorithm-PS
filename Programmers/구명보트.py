렬def solution(people, limit):
	people.sort()
	cnt = 0
	left = 0
	right = len(people) - 1
	while left <= right:
		cnt += 1
		if people[left] + people[right] <= limit:
			left += 1
		right -= 1
	return cnt

print(solution([70,50,80,50], 100))