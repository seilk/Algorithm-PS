# ----------Title
# 니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마-1_20440.py
# Gold IV
# https://www.acmicpc.net/problem/20440

# ----------Tip
# 경계값이 중요한 문제

# ----------URLs
#

# ----------Code with Detail
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

counter = defaultdict(int)

for _ in range(n): #모기들의 입장, 퇴장 시간이 주어짐
    s, e = map(int, input().split())
    counter[s] += 1
    counter[e] -= 1

cntMax = 0
start, end = 0, 0
cur = 0  # 방안의 모기

sorted_counter = sorted(counter.keys()) #시간순으로 정렬
for time in sorted_counter:
    cur += counter[time]  # 방안의 모기 : 모기의 출입이 일어난 시간에서 얼마나 출or입했는지 계산한다.
    if cur > cntMax:  # 계산해주다가 최대값이 나오면 최대 모기 수를 갱신한다.
        cntMax = cur
        start = time  # 최대 모기 수일 때의 시간을 저장한다.

end = start
idx = sorted_counter.index(start)  # 최대 모기일 때의 시간이 저장된 위치
for i in range(idx + 1, len(sorted_counter)):  # 최대 모기 시간이 얼마나 지속되는지 확인 해야함
    if counter[sorted_counter[i]] != 0:  # 모기 수 감소가 일어나는 시간대에서 break
        end = sorted_counter[i]
        break

print(cntMax)
print(start, end)
