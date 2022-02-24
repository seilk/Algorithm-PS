# ----------Title
# 홀수 홀릭 호석
# Gold V
# https://boj.kr/20164

# ----------Tip
# Simulation
# 자연수 분할(순서고려)

# ----------URLs


# ----------Code with Detail
from itertools import combinations_with_replacement as H
from itertools import permutations as P
from itertools import product as PD
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 5 = 1 + 2 + 2 (1 ,2 ,3 ,4, 5) 자연수 분할


def DIVID(s, m):  # 자연수 분할
  n = len(s)
  # B = []
  # A = [tuple(x) for x in H(range(1, n), m) if sum(x) == n]
  D = [tuple(x) for x in PD([i for i in range(1, n)], repeat=3) if sum(x) == n]
  # for a in A:
  #   B += list(P(a, 3))
  # return set(A + B)
  return set(D)


def check(s):
  v = 0
  for i in s:  # s는 string, i는 string의 부분 string
    if int(i) % 2 == 1:
      v += 1
  return v


def make(s, p):
  a, b, c = p
  return [s[:a], s[a:a+b], s[len(s) - c:]]


def DIVIDTWO(s):
  return [s[0], s[1]]


def recursion(s, val):
  global minn
  global maxx

  if len(s) == 1:
    minn = min(val + check(s), minn)
    maxx = max(val + check(s), maxx)
    return

  elif len(s) == 2:
    a, b = DIVIDTWO(s)
    recursion(str(int(a) + int(b)), val + check(s))

  else:
    part = DIVID(s, 3)  # String을 3으로 쪼개는 경우의 수를 모두 구함
    for p in part:
      a, b, c = make(s, p)  # String을 p의 부분으로 쪼갬
      recursion(str(int(a) + int(b) + int(c)), val + check(s))


s = input().rstrip()
minn = 9876543210
maxx = 0
num = ["", "", ""]
recursion(s, 0)
print(minn, maxx)
