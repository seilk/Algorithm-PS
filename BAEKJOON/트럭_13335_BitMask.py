import sys
from collections import deque
input = sys.stdin.readline
numT, brdL, maxW = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bTrucks = deque([])
tCheck = 0
status = 0
t = 0
bW = 0
while tCheck != numT:
    for i in range(brdL - 1, -1, -1):
        if status & (1 << i) == 0:  # i 위치에 트럭이 없을때
            pass
        else:
            status &= ~(1 << i)  # 다리 위의 트럭만 제거
            if i == brdL - 1:
                tCheck += 1
                bW -= bTrucks.popleft()
                continue
            status |= (1 << i + 1)  # 다음칸으로 트럭 이동
    if status & 1 == 0:  # 다리의 첫번째 칸이 남아 있을 떄
        # 현재 이동하지 않은 트럭이 남아있고 다리의 무게를 견딜 수 있을때.
        if trucks and bW + trucks[0] <= maxW:
            bW += trucks[0]  # 다리의 무게에 트럭의 무게 추가
            bTrucks.append(trucks.popleft())
            status |= 1
    t += 1
print(t)

########################################
# x = bin(3)
# y = 0b11
# print(x == y)
# # print(type(x))
# print(bin(int(x, 2) + int(x, 2)))  # 111
