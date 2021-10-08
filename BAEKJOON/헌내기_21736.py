import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
campus = [list(input()) for i in range(n)]
info = [(row, position.index("I")) for row, position in enumerate(
    campus) if "I" in position]  # 마지막 if는 position의 조건
# https://stackoverflow.com/questions/9553638/find-the-index-of-an-item-in-a-list-of-lists
x, y = info[0][0], info[0][1]
queue = deque([(x, y)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS():
    persons = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                nx = x + dx[i]
                ny = y + dy[i]
                if campus[nx][ny] == "P":
                    persons += 1
                # queue에 tuple을 추가해서 나중에 꺼낼때 변수 2개로 받음 #APPEND 되는 순간 queue에 들어가고 나중에 탐색하게 됨.
                if campus[nx][ny] != "X":
                    queue.append((nx, ny))
                    campus[nx][ny] = "X"
                # 탐색한 좌표가 "X"만 아니면 다음 탐색 후보(queue)에 넣어주고 탐색한 좌표는 "X"로 visited 처리를 한다.

    if persons == 0:
        return "TT"
    return persons


print(BFS())
