import sys
from math import comb as C

input = sys.stdin.readline
n, m = map(int, input().split())
print(C(n, m))
