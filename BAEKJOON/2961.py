import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
t = [list(map(int, input().split())) for i in range(n)]
t = [[3, 4]]
# 전부 다 조사
# 인덱스를 일치시켜서 t에 대응 시킴
# n = 4
# 0b10000
# 0b10001 idx - 3
# 0b10010
# 0b10011
# 0b10100
# 0b10101
# 0b10110
# 0b10111
# 0b11000
# --
# 0b11111
# 16
# 사용한다 안한다를 표시.

# 1을 계속 더해주면서 bruteforce 돌리면 될듯.
# 1 떠있는 인덱스 뽑아서
# t[idx][0]끼리 곱하고
# t[idx][1]끼리 더해주면 됨

# 1101
# 1100
cnt = bin(1 << n)  # n개의 자리 확보
miN = 10e9
while True:
    cnt = bin(int(cnt, 2) + 1) 1111 -> 11111
    if len(cnt) == n + 4:
        break
    temp = list(cnt)  # [0,b,1,x,x,x,x,...]
    using = []  # 값이 "1"인 인덱스를 저장하는 곳
    sour = 1  # 곱셈
    bitter = 0  # 덧셈
    for i in range(3, len(temp)):
        if temp[i] == "1":
            using.append(i - 3)

    for j in using:
        sour *= t[j][0]
        bitter += t[j][1]
    miN = min(miN, abs(sour - bitter))
print(miN)
