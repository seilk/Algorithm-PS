import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T = int(In())
seg = [6, 2, 5, 5, 4, 5, 6, 3, 7 ,6]
for t in range(T):
	N = int(In())
	if N % 2 == 0 : print(int("1" * (N//2)))
	else : print(int("7" + "1" * (N//2 - 1)))