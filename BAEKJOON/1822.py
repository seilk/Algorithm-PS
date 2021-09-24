#차집합
from sys import stdin
nA, nB = map(int, stdin.readline().split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
lst = list(A - B); lst.sort()
print(len(lst))
print(*lst) 
