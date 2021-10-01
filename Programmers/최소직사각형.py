import sys


def input() -> str:
    return sys.stdin.readline()


def solution(sizes):
    x = 0
    lst = []
    for i in sizes:
        x = max(x, max(i))  # x is width or height
    for i in sizes:
        y = min(i)
        lst.append(y)
    z = max(lst)
    answer = x * z
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 위클리 8주차
# def solution(sizes):
#     max_x = 0
#     max_y = 0

#     for x, y in sizes:
#         (x, y) = (y, x) if x < y else (x, y)
#         max_x = max(max_x, x)
#         max_y = max(max_y, y)

#     return max_x * max_y
