import sys
N = list(map(int, sys.stdin.readline().rstrip().split()))
A = sys.stdin.readline().rstrip()
if len(A) == N[0]:
    B = sys.stdin.readline().rstrip()
    if len(B) == N[1]:
        print(int(A) * int(B))
        
     