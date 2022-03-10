from collections import defaultdict


def solution(arr) -> list:
    tmp = defaultdict(int)
    for i in range(1, len(arr)):
        tmp[arr[i]] += 1
    print(tmp)
    ans = []
    for k, v in tmp.items():
        if v != 1:
            ans.append(v)
    return ans


print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
