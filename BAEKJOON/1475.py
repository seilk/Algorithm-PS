# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 6->9 9->6
# 숫자에 6 2개 9 1개 있으면 2세트
# 6과 9를 합쳐서 생각 2개당 1세트 3개는 2세트 (2로 나눈 나머지랑 몫을 더함)
# 나머지는 value만큼 필요함
# N <= 10**6, ,자연수, 0
from sys import stdin
import collections
numberlst = [0 for i in range(10)]  # index가 곧 숫자 #숫자가 몇개 들어가는지 기록

nlst = list((stdin.readline().rstrip()))  # ['1', '2', '3'...]
dic = dict(collections.Counter(nlst))  # Counter({'1' : 2, '2' : 3, ...})

for key in dic:
  numberlst[int(key)] = dic[key]

numberlst[9] = ((numberlst[6] + numberlst[9]) // 2) + \
    ((numberlst[6] + numberlst[9]) % 2)
del numberlst[6]
numberset = max(numberlst)
print(numberset)

