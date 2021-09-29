import sys
import math
input = sys.stdin.readline
d = int(input().rstrip())
numbers = list(map(int, input().split()))
opr = list(map(int, input().split()))  # [+, -, *, //] 합이 n-1
oprCheck = [0, 0, 0, 0]  # opr 쓰일때마다 +1
numSet = []  # -10억 ~ 0 ~ 10억


def dfs(depth, z, d):  # -> dfs(depth + 1 , new z), None
    if depth == d - 1:  # 연산자의 개수가 더이상 남아있지 않을 때
        numSet.append(z)
        return
    # depth = 0 numbers[0] (+) numbers[1]
    n = numbers[depth + 1]
    pre = z
    for i in range(4):  # 연산의 개수
        if oprCheck[i] < opr[i]:
            if i == 0:
                z += n
            if i == 1:
                z -= n
            if i == 2:
                z *= n
            if i == 3:
                if z < 0:
                    z = - (-z // n)
                else:
                    z //= n
            oprCheck[i] += 1
            dfs(depth + 1, z, d)
            oprCheck[i] -= 1
            z = pre  # 이전값으로 되돌리고 진행


dfs(0, numbers[0], d)
print(max(numSet))
print(min(numSet))

# 체스 [+ , - , * , //]
# 연산자 더하기
# n = int(input())
# o = ['+', '-', '*', '/']
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # + - * /
# oper = []
# for i in range(4):
#     for j in range(op[i]):
#         oper.append(o[i])
# oper = list(set(permutations(oper, len(oper))))  # 중복제거
