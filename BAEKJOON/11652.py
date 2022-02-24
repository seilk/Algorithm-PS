from sys import stdin
import numpy as np
from collections import Counter
N = int(stdin.readline().rstrip())
joonkyu = []
for i in range(N):
    joonkyu.append(int(stdin.readline().rstrip()))
joonkyu_Counter = Counter(joonkyu).most_common()  #reverse sort[(9, 9), (5, 9), (7, 8) ...]
# print(joonkyu_Counter)
joonkyu_arr = np.array(joonkyu_Counter)
# print(joonkyu_arr)
count_arr = joonkyu_arr[:, 1].copy()
max_count = np.max(count_arr)
# print(max_count) # 등장한 횟수의 최대값
joonkyu_arr_maxSet = joonkyu_arr[joonkyu_arr[:,1] == max_count, 0]
# print(joonkyu_arr_maxSet)
print(joonkyu_arr_maxSet.min())

# print(min(joonkyu_arr)

