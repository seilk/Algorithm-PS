import sys
import math

def In() : return sys.stdin.readline().rstrip()

def MIS() : return map(int, In().split())

def func() :
	global ans

	for i in range(1, n+1) :
		for j in range(1, m+1) :
			for a in range(-n, n) :
				for b in range(-m, m) :
					if a == 0 and b == 0 : continue  # 자기 자신을 나타내므로 배제
					cx, cy = i, j
					cur = ""
					while 1<=cx<=n and 1<=cy<=m :
						cur += str(table[cx][cy])
						if cur != "" and int(math.sqrt(int(cur)))**2 == int(cur) :
							ans = max(ans, int(cur))
						cx += a
						cy += b

n, m = MIS()
table = [[0] * (m+1)] + [ [0] + [ *map(int, list(In())) ] for i in range(n) ]
ans = -1
func()
print(ans)
