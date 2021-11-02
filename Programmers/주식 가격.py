from collections import deque


def solution(prices):
    ans = [0] * len(prices)
    queue = deque(prices)
    stack = deque([])
    t = 0
    while queue:
        x = queue.popleft()
        tmp = []
        if stack:
            while stack:
                info = stack.popleft()
                value, timeidx = info[0], info[1]
                if value > x:
                    ans[timeidx] = t - timeidx  # idx
                else:
                    tmp.append(info)
        tmp.append([x, t])
        stack = deque(tmp.copy())
        t += 1
    for info in (stack):
        if not ans[info[1]]:
            ans[info[1]] = t - 1 - info[1]

    # slide = deque([])
    # slide.appendleft(prices.pop())
    # timeLine = deque([0])
    # for i in range(len(prices) - 1, -1, -1):
    #     x = prices.pop()
    #     if x <= min(slide):
    #         timeLine.appendleft(len(slide))
    #         slide.appendleft(x)
    #         continue
    #     for i in range(len(slide)):
    #         if x > slide[i]:
    #             slide.appendleft(x)
    #             timeLine.appendleft(i + 1)
    #             break

    # 해당시간의 가격과 이전 시간의 가격들을 비교해야하는 문제
    # 시간은 idx로 생각한다
    # 뒤에서 부터 체크

    return ans


# print(solution([1, 2, 3, 2, 3]))
print(solution([5, 8, 6, 2, 4, 1]))

#AC

def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans