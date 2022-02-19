#파이썬 정수형 처리 조심... int() 남발 하지 않기
import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T = int(In())
for t in range(T):
  n,k=MIS()
  if n > k:
    print(((4*n+4)*n//2)-((4*(n-k-1)+4)*(n-k-1)//2))
  else: print(int((4*n+4)*n//2))

# n=1 -> 4 = 4
# n=2 -> 4 + 8 = 12
# n=3 -> 4 + 8 + 12 = 24
# n=4 -> 4 + 8 + 12 + 16 = 40
# n=5 -> 4 + 8 + 12 + 16 + 20 = 60
# n=6 -> 4 + 8 + 12 + 16 + 20 + 24 = 84