# 서로 다른 양의 정수이므로 오름차순 배열해주고 이진탐색으로도 풀이 가능.
import sys
input = sys.stdin.readline
size = int(input().rstrip())
seq = list(map(int, input().split()))
goal = int(input().rstrip())
cnt = 0
board = [0] * 2_000_001  # goal의 최대 크기 = 2,000,000, +1 = index와 value값 일치
for i in seq:
    board[i] = 1  # O(N)

for i in seq:
    if board[goal - i]:
        cnt += 1
        # goal = 2 i = 100000

print(int(cnt // 2))  # 0 / 2 = 0.0

# 0 // 2 = 0


# input = sys.stdin.readline
# size = int(input().rstrip())
# seq = list(map(int, input().split()))
# goal = int(input().rstrip())
# cnt = 0
# board = [0] * 2_000_001  # index와 value값 일치시킴

# # for i in seq:
#    if goal > i and board[goal - i]:
#         cnt += 1
#     board[i] = 1
# print(cnt)

'''
9
5 12 7 10 9 1 2 3 11
13
'''
