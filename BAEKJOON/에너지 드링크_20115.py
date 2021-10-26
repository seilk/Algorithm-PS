import sys
from collections import deque
# input = lambda: sys.stdin.readline().rstrip()
def input(): return sys.stdin.readline().rstrip()


# 버리는 양을 최소화
n = int(input())
amount = list(map(int, input().split()))
# 가장 적은거를 붓는쪽으로 한다.
amount.sort()
amount = deque(amount)  # 오름차순으로 정렬
# i번째를 i + 1번째에 붓는것을 반복
while len(amount) > 1:

    p = amount.popleft()
    amount[-1] += p / 2
print(amount[0])
# 3 2 10 9 6
# 2 3 6 9 10
# 3 6 9 11
# 6 9 12.5
# 9 15.5
