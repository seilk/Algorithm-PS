import sys
from collections import deque

# 이런문제는 BFS 문제가 아니다.


def input():
    return sys.stdin.readline().rstrip()


d = int(input())
farm = [list(map(int, input().split())) for i in range(d)]
visited = [[0] * d for i in range(d)]
queue = deque([])
prices = set()
ddx = [1, -1, -1, 1]
ddy = [1, -1, 1, -1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS():
    for a in range(1, (d - 1)):
        for b in range(1, (d - 1)):
            seed = 2
            visited[a][b] = 1
            price = farm[a][b]
            for j in range(4):
                cx = a + dx[i]
                cy = b + dy[i]
                visited[cx][cy] = 1
                price += farm[cx][cy]
            queue.append((a, b))

            while queue:
                while seed > 0:
                    x, y = queue.popleft()
                    for i in range(4):
                        if 1 <= x + ddx < d - 1 and 1 <= y + ddy < d - 1:
                            nx = x + ddx[i]
                            ny = y + ddy[i]
                            if not visited[nx][ny]:
                                flower = True
                                for k in range(4):
                                    if visited[x + dx[k]][y + dy[k]]:
                                        flower = False
                            if flower:
                                visited[nx][ny] = 1
                                price += farm[nx][ny]
                                seed -= 1
                                for j in range(4):
                                    cx = nx + dx[i]
                                    cy = ny + dy[i]
                                    visited[cx][cy] = 1
                                    price += farm[cx][cy]
                            queue.append((nx, ny))
                seed += 1
            prices.add(price)
            queue = deque([])
            visited = [[0] * d for i in range(d)]
            price = 0


print(min(prices))
