import sys
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
pocket = set()
visited = [0] * n


def DFS(answer):
    if len(answer) == m:
        pocket.add(tuple(answer))
        return
    for i in range(n):
        if visited[i] or (answer and answer[-1] > numbers[i]):
            continue
        visited[i] = 1
        DFS(answer + [numbers[i]])
        visited[i] = 0


DFS([])
pocket_list = sorted(list(pocket))
for series in pocket_list:
    print(*series)
