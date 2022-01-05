# ----------Title
# 곱셈
# Silver I
# https://boj.kr/1629

# ----------Tip
# 분할정복을 이용한 거듭제곱
# pow(a,b,c)
# 일반적인 n번 거듭제곱은 O(n)이지만 이를 분할정복으로 O(log(N))으로 줄일 수 있다.
# ----------URLs
# https://www.acmicpc.net/board/view/70289
# https://torbjorn.tistory.com/361

# ----------Code with Detail
import sys

sys.setrecursionlimit(10 ** 6)
a, b, c = map(int, input().split())


def binpow(a, b):
  if b == 0:
    return 1
  res = binpow(a, b // 2)
  if b & 1:
    return (res * res * a) % c
  else:
    return (res * res) % c


print(binpow(a, b))
