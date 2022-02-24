from sys import stdin
from collections import deque

# q = deque()
# p = deque()
# p.append(['a', 'b'])
# print(p)
# print(q)
# print(p[0][0])
# print(q[0][0])

n = int(stdin.readline().rstrip())
jelly = [0 for i in range(n)]
for i in range(n):
    jelly[i] = list(map(int, stdin.readline().split()))

x, y = 0, 0
queue = deque()
queue.append((x, y))  # 2차원 좌표를 deque에 입력
while True:
    if len(queue) == 0:
        print("Hing")
        break

    if (n - 1, n - 1) in queue:  # (n - 1 , n - 1) 좌표가 queue에 있으면 성공
        print("HaruHaru")
        break

    value = jelly[queue[0][0]][queue[0][1]]
    if 0 <= queue[0][0] + value < n:
        if (queue[0][0] + value, queue[0][1]) not in queue:
            queue.append((queue[0][0] + value, queue[0][1]))  # x좌표만 변한 좌표를 deque에 입력

    if 0 <= queue[0][1] + value < n:
        if (queue[0][0], queue[0][1] + value) not in queue:
            queue.append((queue[0][0], queue[0][1] + value))  # y좌표만 변한 좌표를 deque에 입력
    queue.popleft()
