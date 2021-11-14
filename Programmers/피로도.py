answer = -1


def solution(k, dungeons):
    visited = [0] * len(dungeons)
    DFS(dungeons, k, 0, visited)
    return answer


def DFS(dungeons, tired, cnt, visited):
    global answer
    for i in range(len(dungeons)):
        if not visited[i] and (tired >= dungeons[i][0]):
            visited[i] = 1
            DFS(dungeons, tired - dungeons[i][1], cnt + 1, visited)
            visited[i] = 0
    answer = max(cnt, answer)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

# def DFS(depth, lst, visited):
#     if depth == len(lst):
#         return

#     for i in range(n):
#         visited[i] = 1
#         DFS(depth + 1, lst, visited)
#         visited[i] = 0
#         lst.pop()
