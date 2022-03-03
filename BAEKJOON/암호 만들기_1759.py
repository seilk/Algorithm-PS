import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def backTracking(word, d, x, y, idx):
	global ans
	if d == L:
		if x >= 1 and y >= 2: # 최소 한개의 모음과 두개의 자음
			ans.append(word)
	for i in range(idx, C): # 오름차순 보장
		if not vist[i]:
			vist[i] = 1
			if arr[i] in ['a', 'e', 'i', 'o', 'u']:
				backTracking(word + arr[i], d+1, x+1, y, i)
			else :
				backTracking(word + arr[i], d+1, x, y+1, i)
			vist[i] = 0

L, C = MIS() # 암호의 길이, 주어지는 정수의 개수
arr = In().split()
arr.sort()
ans = []
vist = [0] * C
backTracking("", 0, 0, 0, 0)
print(*ans, sep = "\n")