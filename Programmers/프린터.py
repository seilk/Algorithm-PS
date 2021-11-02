from heapq import *
from collections import deque


def solution(prior, loc):
    ans = [val, idx] = [1, 4]
    ans = [prior[loc], loc]
    stack = deque([[v, i] for i, v in enumerate(prior)])
    pq = [[-v, i] for i, v in enumerate(prior)]
    heapify(pq)
    # y = [1, 2, 10, 14, 3, 5]
    # z = [-1, -2, -10, -14, -3, -5]
    # heapify(y)  # print 순서 : 1, 2, 3, 5, 10, 14
    # heapify(z)  # -14 -10 -5 -3 -2 -1
    # while y:
    #     print(heappop(y)) #작은거 -> 큰거
    #     print(-heappop(z))
    cnt = 0
    while pq:
        slide = deque([])
        item = heappop(pq)
        val, idx = -item[0], item[1]
        x = stack.popleft()
        while x[0] != val:
            slide.append(x)
            x = stack.popleft()
        cnt += 1
        if x == ans:
            return cnt
        stack = stack + slide
    return cnt


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

lst = [[1, 2], [3, 4], [5, 1], [3, 9], [4, 19]]
print(max(lst, key=lambda x: x[1])[1])
