from sys import stdin
import collections

n = int(stdin.readline().rstrip())
queue = collections.deque([])
temp_queue = collections.deque([])
for _ in range(n):
    gangsan = list(stdin.readline().rstrip())
    for i in range(len(gangsan)):
        if gangsan[i] == "-":
            if queue:
                queue.pop()
            continue

        elif gangsan[i] == "<":
            if queue:
                temp_queue.appendleft(queue.pop())
            continue

        elif gangsan[i] == ">":
            if temp_queue:
                queue.append(temp_queue.popleft())
            continue

        else:
            queue.append(gangsan[i])

    print(*(queue + temp_queue), sep="")
    queue = collections.deque([])
    temp_queue = collections.deque([])
