import sys
In = lambda : sys.stdin.readline().rstrip()


def hanoi(n, start, end, mid):
	if n == 1:
		print(start, end)
		return
	hanoi(n - 1, start, mid, end)
	print(f"{start} {end}")
	hanoi(n - 1, mid, end, start)

def count(n):
	return 2**n - 1

N = int(In())
print(count(N))
if N <= 20:
	hanoi(N, 1, 3, 2)
