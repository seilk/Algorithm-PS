import sys
input = sys.stdin.readline
size = int(input().rstrip())
seq = list(map(int, input().split()))
goal = int(input().rstrip())
cnt = 0


def boj3273(p1, p2, lst, goal):  # -> None or boj3273(p1 + 1, p1 + 2, lst, goal)
    global cnt
    while lst.count(-1) != size:
        if p2 == size:
            lst[p1] = -1
            p1 += 1
            p2 = p1 + 1
            continue
        elif lst[p2] == -1:
            p2 += 1
            continue
        elif lst[p1] == -1:
            p1 += 1
            p2 = p1 + 1
        elif lst[p1] + lst[p2] == goal:
            cnt += 1
            lst[p1] = -1
            lst[p2] = -1
            p1 += 1
            p2 = p1 + 1
            continue
        p2 += 1
    return cnt


print(boj3273(0, 1, seq, goal))

'''
9
5 12 7 10 9 1 2 3 11
13
'''
