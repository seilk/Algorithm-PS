import sys
from collections import deque
input = sys.stdin.readline
numT, brdL, maxW = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bTrucks = deque([])
tCheck = 0


def f(a: bin, b: bin, o: str) -> bin:
    if o == "xor":
        return(bin(int(a, 2) ^ int(b, 2)))
    elif o == "or":
        return(bin(int(a, 2) | int(b, 2)))
    elif o == "and":
        return(bin(int(a, 2) & int(b, 2)))


x = bin(1 << brdL)  # 1(00) #000
t = 0
bW = 0
# 0b100
while tCheck != numT:
    for i in range(3, len(x)):
        if i != 3 and x[i] == '1':
            # 이진수{2진수(1) -> 정수 (계산) 2진수(2) -> 정수}
            x = bin(int(x, 2) + int(bin(1 << (len(x) - 1 - i)), 2))
        if i == 3 and x[i] == '1':
            x = bin(int(x, 2) - int(bin(1 << brdL - 1), 2))
            tCheck += 1
            bW -= bTrucks.popleft()
    if x[-1] == "0":
        if trucks and bW + trucks[0] <= maxW:
            # 첫번째 칸으로 트럭을 이동시킨다
            bW += trucks[0]
            bTrucks.append(trucks.popleft())
            x = bin(int(x, 2) + int(bin(1), 2))
        else:
            pass
    t += 1
print(t)

x = bin(1 << 3)  # 1000
y = bin(int(x, 2) ^ int(bin(1), 2))  # 1000 vs 0001
print(y)

########################################
# x = bin(3)
# y = 0b11
# print(x == y)
# # print(type(x))
# print(bin(int(x, 2) + int(x, 2)))  # 111
