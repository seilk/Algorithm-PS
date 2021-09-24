# 오름차순인 Series에서 max와 min의 차이는 max와 min 사이에 있는 값들의 차이의 합이다.

import sys
from sys import stdin
n, k = map(int, stdin.readline().split())
tall = list(map(int, stdin.readline().split()))
diff = []
for i in range(1, n):
    diff.append(tall[i] - tall[i - 1])

diff.sort(reverse=True)
print(sum(diff[k - 1:]))
    

 
# lst = [[1], [3,4],[], []]
# lst.sort(reverse = True)
# print(lst.index([]))
# print(lst)

