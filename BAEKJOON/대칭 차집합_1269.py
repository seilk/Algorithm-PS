from sys import stdin
nA, nB = map(int, stdin.readline().split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
print(len(A - B) + len(B - A))