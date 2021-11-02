import sys
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
ans = list(permutations(numbers, m))
ans2 = list(set(ans))
ans2.sort()
for series in ans2:
    ans3 = list(series)
    print(*ans3)
