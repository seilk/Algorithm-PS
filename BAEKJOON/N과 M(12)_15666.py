import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
# n개의 자연수, 자연수 m
# 길이가 m인 수열
# n개의 자연수 중에서 m개를 고른 수열
# 중복 가능
# 비 내림차순 (크거나 같은)
# lst에서 하나씩 뽑아서 만들고 길이 충족하면 pop
# 뽑는 조건은 lst에 들어간 수보다 같거나 큰 숫자로
# dfs
ansSet = set()
ans = []


def DFS(depth):
    if depth == m:
        ansSet.add(tuple(ans))
        return
    for i in range(len(lst)):
        if ans == []:
            ans.append(lst[i])
        elif ans[-1] > lst[i]:
            continue
        elif ans[-1] <= lst[i]:
            ans.append(lst[i])
        DFS(depth + 1)
        ans.pop()


DFS(0)
ansList = list(ansSet)
ansList.sort()
for i in ansList:
    print(*i, sep=" ")

# 주의 : 문자열 sort는 1 < 11 < 7 임!
