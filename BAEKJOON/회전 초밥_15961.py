import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N, d, k, c = MIS() # 접시 수, 종류의 수, 연속 수, 쿠폰
sushi = [int(In()) for i in range(N)]
sushi += sushi # index == N 일 때 처음으로 돌아오게 됨
vist = [0] * 3001 # 초밥 종류의 개수 저장
vist[c] = 1
left, right = 0, 0
mxx = -1
typ = 1
while left <= N:
	if right - left + 1 > k :
		if vist[sushi[left]] == 1:
			typ -= 1
		vist[sushi[left]] -= 1
		left += 1
	else :
		if vist[sushi[right]] == 0:
			typ += 1
		vist[sushi[right]] += 1
		right += 1
	mxx = max(mxx, typ)
print(mxx)


# 7 9 7 30 2 7 9 25 7 9 7 30 2 7 9 25
