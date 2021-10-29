from collections import defaultdict
from itertools import combinations

# def solution(orders, course):
#     answer = []
#     for num in course:
#         dic = defaultdict(int)
#         for order in orders:
#             visited = [0] * len(order)
#             ans = []
#             DFS(0, num, order, visited, dic, ans)
#         m = max(list(dic.values()), key=lambda x: x > 1)
#         print(m)
#         for k, v in dic.items():
#             if v == m:
#                 answer.append(k)
#     answer.sort()
#     return answer


# def DFS(depth, num, order, visited, dic, ans):
#     if depth == num:
#         dic["".join(ans)] += 1
#         return
#     for j in range(len(order)):
#         if not visited[j]:
#             visited[j] = 1
#             ans.append(order[j])
#             DFS(depth + 1, num, order, visited, dic, ans)
#             ans.pop()
#             visited[j] = 0

def solution(orders, course):
    answer = []
    for num in course:
        dic = defaultdict(int)
        for order in orders:
            tuples = list(combinations(list(order), num))
            for val in tuples:
                x = list(val)
                x.sort()
                dic["".join(x)] += 1

        if dic.values():
            m = max(list(dic.values()))
            if m > 1:
                for k, v in dic.items():
                    if v == m:
                        answer.append(k)
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 5]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
