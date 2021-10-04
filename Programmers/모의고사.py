from collections import deque


def solution(answers):
    queue = deque(answers)
    score = [0, 0, 0, 0]
    p1 = deque([1, 2, 3, 4, 5])
    p2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    p3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    pSet = [0, p1, p2, p3]
    while queue:  # BFS
        ans = queue.popleft()
        for i in range(1, 4):
            s = pSet[i].popleft()
            score[i] += 1 if ans == s else 0
            pSet[i].append(s)

    maxVal = max(score)
    sol = []
    for i, v in enumerate(score):
        if i != 0 and maxVal == v:
            sol.append(i)
    sol.sort()
    return sol
