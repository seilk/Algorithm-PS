from sys import stdin
from collections import Counter
N = int(stdin.readline().rstrip())
joonkyu = []
for i in range(N):
    joonkyu.append(int(stdin.readline().rstrip()))
# descending countNumber sort[(9, 9), (5, 9), (7, 8) ...]
joonkyu_Counter = Counter(joonkyu).most_common()
joonkyu_Counter.sort(key=lambda x: (-x[1], x[0]))
print(joonkyu_Counter[0][0])

# import sys
# input = sys.stdin.readline
# n = int(input())
# a = [int(input()) for _ in range(n)]
# a.sort()
# s, cnt, ans_cnt, ans = a[0], 0, 1, a[0]
# for x in a:
#     if s == x:
#         cnt += 1
#     else:
#         s = x
#         cnt = 1
#     if cnt > ans_cnt:
#         ans_cnt = cnt
#         ans = x
# print(ans)

#######################################

# import sys

# input = sys.stdin.readline

# freq = {}

# for _ in range(int(input())):
#     num = int(input())
#     if freq.get(num) == None:
#         freq[num] = 1
#     else:
#         freq[num] += 1

# max_freq = max(freq.values())

# temp = []
# for k, v in freq.items():
#     if v == max_freq:
#         temp.append(k)

# print(min(temp))
