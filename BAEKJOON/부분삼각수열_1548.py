import sys
# from itertools import combinations
def input(): return sys.stdin.readline().rstrip()


# 삼각수열이 없을 때는 2를 출력한다.
# 정해진 수열에서 3개의 수를 뽑았을때 2개의 합이 남은 1개보다 커야한다.
# 3번 검사해야함.
# 3개의 수에서 가장 큰 수 > 두 수의 합 이면 삼각수열
n = int(input())
ini = list(map(int, input().split()))
ini.sort()


def find(lst):
    for i in range(0, n - 2):
        a, b = ini[i], ini[i + 1]
        if a + b > ini[-1]:
            return i, i + 1
    return None, None


x, y = find(ini)
if x == None:
    print(2 if len(ini) > 1 else 1)
else:
    print(len(ini) - y + 1)
# stack = []
# visited = [0] * n
# 1233445

# def isTriangle(x, y, z) -> bool:
#     if x + y <= z:
#         return False
#     if x + z <= y:
#         return False
#     if y + z <= x:
#         return False
#     return True


# def check(lst) -> bool:
#     x = list(combinations(lst, 3))
#     for piece in x:
#         if not isTriangle(piece[0], piece[1], piece[2]):
#             return False
#     return True


# def DFS(stack, maxLeng):
#     if len(stack) >= 3 and check(stack):
#         maxLeng = max(maxLeng, len(stack))
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = 1
#             maxLeng = DFS(stack + [ini[i]], maxLeng)
#             visited[i] = 0
#     return maxLeng


# if n > 2:
#     print(DFS([], 2))
# else:
#     print(n)
