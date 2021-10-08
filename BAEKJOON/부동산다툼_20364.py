from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


t, d = map(int, input().split())
want = [int(input()) for i in range(d)]
# 1번 노드 = 2 * 1, 2 * 1 + 1
# 2번 노드 = ""
graph = [[2 * i, 2 * i + 1] for i in range(2 ** 20)]
graph[0] = [0, 0]
# graph의 인덱스는 노드의 번호와 동일하다.
stack = deque([])
# 이진트리의 부모는 해당 노드의 //2 와 동일하다.

for i in want:  # 원하는 땅을 loop
    d = i
    while d != 1:
        stack.appendleft(d)  # 6 (1 3 6) # 12 (1,3,6,12)
        d //= 2

    for j in stack:
        if graph[j] == []:
            print(j)
            break
        if j == i:
            graph[i] = []
            print(0)
            break


#########AC##########
'''
import sys
input = sys.stdin.readline

def check(idx):
    i = duck[idx]
    val = 0
    while i > 0:
        if occupied[i] == 1:
            val = i
        i //= 2
    if val == 0:
        occupied[duck[idx]] = 1 
    duck[idx] = val


if __name__ == "__main__":
    n, q = map(int, input().split())
    occupied = [0]*(n+1)
    duck = [int(input()) for _ in range(q)]
    for i in range(q):
        check(i)
    
    for i in range(q):
        print(duck[i])
'''
####################
