import sys

"""
핵심은 인접행렬을 인접리스트로 전처리 해주는것
모든 노드를 대상으로 bfs를 한번씩 실행시킴
시간복잡도는 N^3으로 플로이드-와샬 풀이와 동일함
"""
def sol():
    input = sys.stdin.readline
    N = int(input())
    node = [[] for i in range(N)]
    for i in range(N):
        vector = list(map(int, input().split(" ")))
        for j in range(N):
            if vector[j] == 1:
                node[i].append(j)
    for i in range(N):
        print(" ".join(bfs(N, node, i)))


def bfs(N, node, i):
    queue = []
    visited = [False] * N
    queue.append(i)
    while len(queue) > 0:
        v = queue.pop(0)
        for w in node[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
    result = []
    for check in visited:
        if check:
            result.append("1")
        else:
            result.append("0")
    return result


if __name__ == "__main__":
    sol()
