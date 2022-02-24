# BOJ_2225, 합분해
# Tip : Dynamic Programming
import sys
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
# cache에는 i를 k번 사용해서 만드는 개수가 들어간다.
cache = [[1] * (k + 1)] + [[0] * (k + 1) for i in range(n)]
mod = 1_000_000_000
for row in range(1, n + 1):
  for col in range(1, k + 1):
    cache[row][col] = (cache[row - 1][col] + cache[row][col - 1]) % mod

print(cache[n][k])
# for i in range(n):
#   # for j in range(i // 2 + 1):
#   #   cache[i] = cache[i - j] + cache[j] +

# cache[i] += len(list(product([n, 0, 0, 0], k)))
# print(ans % 10**9)
# 6을 구하는데 2를 안다고 해서 도움이 되나? 이 접근이 아닌듯
# 2를 안다는 것 ? : 2를 0, 1, 2 를 4번써서 구하는 경우의 수?
# 모자란 개수는 0으로 채우면 됨
# 결국 문제는 분할되어 n을 k개로 쪼개는 방법의 수로 분할됨
# 정확히 말하자면 1개 2개 3개 ... k개로 쪼개는 방법의 수로 분할 (k개는 0없이)
