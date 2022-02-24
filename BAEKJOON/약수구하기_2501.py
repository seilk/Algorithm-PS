# ----------Title
# 약수구하기
# Bronze III
# https://www.acmicpc.net/submit/2501

# ----------Tip
# Mathmatics


# ----------URLs


# ----------Code with Detail
import sys
import heapq
import math
input = sys.stdin.readline


def findDiv(n):
  divisors = set()
  t = int(math.sqrt(n))
  for i in range(1, t + 1):
    if n % i == 0:
      divisors.add(i)
      divisors.add(n // i)
  return sorted(list(divisors))


if __name__ == "__main__":
  n, k = map(int, input().split())
  pars = findDiv(n)
  try:
    print(pars[k - 1])
  except:
    print(0)

# ----------Why Wrong...?
  # if k > len(pars):
  #   print(0)
  # else:
  #   for _ in range(k - 1):
  #     heapq.heappop(pars)
  #   print(heapq.heappop(pars))
