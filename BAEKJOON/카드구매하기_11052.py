import sys
import copy
def input(): return sys.stdin.readline().rstrip()


n = int(input())  # n개를 사는데 최대한 많은 돈을 소비하기
price = [0] + list(map(int, input().split()))
cache = copy.deepcopy(price)

# for i in range(2, n + 1):
#   for j in range(1, i):
#     cache[i] = max((i//j) * cache[j] + cache[i % j], cache[i])
# print(cache[-1])

# 두번째 for문을 절반만 탐색하는 방법
# cache[i] 에는 카드 i개를 구매하는데 최대 비용이 저장
# cache[1] = price[1]
# cache[2] = max(price[2], cache[1] + cache[1])
# cache[3] = max(price[3], cache[1] + cache[2], cache[2] + cache[1])
# 이 때 (1,2)와 (2,1)은 같은 순서쌍이므로 중복을 제외시켜주기 위해서 절반만 탐색함.
for i in range(2, n + 1):
  for j in range(1, i // 2 + 1):
    cache[i] = max(cache[j] + cache[i - j], cache[i])
print(cache[-1])
