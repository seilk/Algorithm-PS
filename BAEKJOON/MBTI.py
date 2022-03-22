import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def initMBTIset():
	first = ["E", "I"]
	second = ["N", "S"]
	third = ["F", "T"]
	fourth = ["J", "P"]
	mbtiSet = set()
	for m in first:
		for b in second:
			for t in third:
				for i in fourth:
					mbtiSet.add(m+b+t+i)
					mbtiSet.add(i+t+b+m)
	return mbtiSet

N,M = [*MIS()]
mbtiSet = initMBTIset()
board = [list(In()) for i in range(N)]
ans = 0
for n in range(N):
	for m in range(M):
		#1. 가로
		if m + 3 < M:
			s1 = "".join(board[n][m:m+4])
			if s1 in mbtiSet:
				ans+=1
				
		#2. 세로
		if n + 3 < N:
			s2 = "".join(list(board[i][m] for i in range(n, n + 4)))
			if s2 in mbtiSet:
				ans+=1
				
		#3. 대각선1
		if n + 3 < N and m + 3 < M:
			s3 = "".join(list(board[n+i][m+i] for i in range(4)))
			if s3 in mbtiSet:
				ans+=1
				
		#4. 대각선2
		if n + 3 < N and 0 <= m - 3:
			s4 = "".join(list(board[n+i][m-i] for i in range(4)))
			if s4 in mbtiSet:
				ans+=1
				
print(ans)