import sys

input = sys.stdin.readline
import collections

n = int(input())

counter = collections.defaultdict(int)

for _ in range(n):
    s, e = map(int, input().split())
    counter[s] += 1
    counter[e] -= 1

cntMax = 0
start, end = 0, 0
cur = 0  # 방안의 모기

sorted_Counter = sorted(counter.keys())
for time in sorted_Counter:
    cur += counter[time]  # 방안의 모기 : 모기의 출입이 일어난 시간에서 얼마나 출or입했는지 계산한다.
    if cur > cntMax:  # 계산해주다가 최대값이 나오면 최대 모기 수를 갱신한다.
        cntMax = cur
        start = time  # 최대 모기수일 때의 시간을 저장한다.

end = start
idx = sorted_Counter.index(start)  # 최대 모기일 때의 시간이 저장된 위치
for i in range(idx + 1, len(sorted_Counter)):  # 최대모기 시간이 얼마나 지속되는지 확인해야함
    if counter[sorted_Counter[i]] != 0:  # 변화(모기 수 감소)가 일어나는 시간대에서 break
        end = sorted_Counter[i]
        break

print(cntMax)
print(start, end)
