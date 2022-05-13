import sys

In = lambda:sys.stdin.readline().rstrip()
MIS = lambda:map(int,In().split())


def check(i,j,a,b,K):
	return a*i+b*j

def swap(x, y):
	return y, x
# O(NlogN)
def solve(a,b,K):
	for x in range(1, K + 1):
		left = 1
		right = K
		while left <= right:
			mid = (left+right)//2
			now = check(x,mid,a,b,K)
			if now > K:
				right = mid-1
			elif now == K:
				if x > mid:
					x, mid = swap(x, mid)
				return x, mid
			else:
				left = mid+1


D,K = MIS()
dp = [ [ 0,0 ] for i in range(31) ]
dp[ 1 ] = [ 1,0 ]
dp[ 2 ] = [ 0,1 ]
for d in range(3,31):
	dp[ d ][ 0 ] = dp[ d-2 ][ 0 ]+dp[ d-1 ][ 0 ]
	dp[ d ][ 1 ] = dp[ d-2 ][ 1 ]+dp[ d-1 ][ 1 ]
a,b = dp[ D ]
# print(f"{a}, {b} is dp[D]")
xx,yy = solve(a,b,K)
print(f"{xx}\n{yy}")
