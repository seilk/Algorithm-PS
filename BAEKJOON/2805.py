import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()


def cut(start, end, lst):  # -> cut(new_s, new_e, lst) or mid
    global m
    mid = (start + end) // 2  # 절단기에 설정한 높이
    height = 0
    for i in lst:
        if mid < i:
            height += i - mid
    if height == m:  # 적어도 m
        return mid
    if start > end and height >= m:  # start와 end가 맞물리는 경우가 있을 수 있음.
        return mid
    if height > m:  # 잘린 나무의 길이가 m보다 크면 높이를 더 늘려도 됨.
        return cut(mid + 1, end, lst)
    else:  # 잘린 나무의 길이가 m보다 작으면 높이를 낮춰야함.
        return cut(start, mid - 1, lst)


print(cut(0, trees[-1], trees))

# def cutt(start, end, lst): #-> height
#     height = 0
#     while height != m:
#         mid = (start + end) // 2
#         for i in lst:
#             if mid < i:
#                 height += i - mid
#         if height > m:
#             start = mid + 1
#             end = end
#             height = 0
#         else:
#             start = start
#             end = mid - 1
#             height = 0
#     return height


# print(cutt(0, 1_000_000_000, trees))


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst[:] = [x for x in lst if x > 5]
# print(lst)
