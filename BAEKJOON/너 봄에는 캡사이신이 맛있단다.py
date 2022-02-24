import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def fpow(a,x):
  res = 1
  while x:
    if x & 1:
      res = res*a%MOD
    a=a*a%MOD
    x>>=1
  return res

N = int(In())
arr = [*MIS()]
arr.sort()
MOD = 1_000_000_007

ans=0
for i in range(N):
  a=(arr[i]%MOD) * fpow(2, i)%MOD
  ans+=a

  b=(arr[i]%MOD) * fpow(2, N-i-1)%MOD
  ans-=b

  ans = ((ans%MOD)+MOD)%MOD
print(ans)
# 모든 조합의 (최대값-최소값)의 합
# = 모든 i에 대해서 : (i가 최대값일때 조합의 수 * i) - (i가 최소값일떄의 조합의 수 * i)
# (A + B) % p = ((A % p) + (B % p)) % p
# (A * B) % p = ((A % p) * (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p
