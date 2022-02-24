# ----------Title
# Aftermath
# Gold V
# https://www.acmicpc.net/problem/19303

# ----------Tip
# Mathmatice
# Divisor

# ----------URLs


# ----------Code with Detail
import sys
import statistics

input = sys.stdin.readline


def find_div(n):
  if n == 0:
    return [0]
  divisors = []
  k = int(n ** 0.5)
  for i in range(1, k + 1):
    if not (n % i):
      divisors += [i, n // i]
  return divisors


if __name__ == "__main__":
  a = int(input().rstrip())
  h = int(input().rstrip())
  MAXIMUM = 10 ** 15
  for n in range(0, MAXIMUM + 1):
    pars = find_div(n)
    tmpa = statistics.mean(pars)
    tmph = statistics.harmonic_mean(pars)
    if a == tmpa and h == tmph:
      print(n)
      break

# def cala(pars, l):
#   if pars == [0]:
#     return 0
#   return (sum(pars) / l)


# def calh(pars, l):
#   if pars == [0]:
#     return 0
#   tmp = 0
#   for p in pars:
#     tmp += (1 / p)
#   return (tmp / l) ** -1
