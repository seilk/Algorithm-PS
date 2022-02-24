import sys
def input(): return sys.stdin.readline().rstrip()


d = int(input())
farm = [list(map(int, input().split())) for i in range(d)]
visited = [[0] * d for i in range(d)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
minPrice = 3000


def DFS(depth, price) -> int:
    global minPrice
    if depth == 3: #기저 조건
        if minPrice > price:
            minPrice = price
        return
    for i in range(1, d - 1): #모서리 부분 배제
        for j in range(1, d - 1):
            if not visited[i][j]:  # (i, j)가 방문한곳이 아니면
                if checkNeighbor(i, j):
                    pre = price
                    visited[i][j] = 1
                    price += farm[i][j]
                    for k in range(4):
                        visited[i + dx[k]][j + dy[k]] = 1
                    for k in range(4):
                        price += farm[i + dx[k]][j + dy[k]]
                    DFS(depth + 1, price)
                    visited[i][j] = 0
                    for k in range(4):
                        visited[i + dx[k]][j + dy[k]] = 0
                    price = pre  # 가격 이전 가격으로 맞춰줌.


def checkNeighbor(i, j):
    flower = True
    for k in range(4):  # 상하좌우 visited 확인
        if visited[i + dx[k]][j + dy[k]]:
            flower = False
    return flower


DFS(0, 0)
print(minPrice)
