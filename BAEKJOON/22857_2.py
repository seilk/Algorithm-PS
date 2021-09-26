# Two Pointer
from itertools import combinations
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
l, d = map(int, input().split())
srs = list(map(int, input().split()))
srs_e = [1 if i % 2 == 0 else 0 for i in (srs)]  # 짝수면 1 홀수면 0으로 변환
count = 0
maxValue = 0


def f(start):
    global count
    global l
    global maxValue
    value = 0
    if start > l - 1:
        return
    for i in range(start, l):
        if srs_e[i] % 2:  # srs_e의 원소가 짝수일 때 value값 증가시킴
            value += 1
        else:  # srs_e의 원소가 홀수일 때
            count += 1  # count값 증가시킴
            if count == d + 1:  # count가 삭제 최대 횟수보다 커질 때
                count = 0
                break
    maxValue = max(value, maxValue)
    return f(start + 1)  # 이전의 start값보다 +1의 값으로 재귀함수


f(0)
print(maxValue)

# p = [1, 2, 3, 4, 5, 6]
# print(list(combinations(p, 4)))
