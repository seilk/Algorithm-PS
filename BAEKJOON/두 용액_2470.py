import sys
def input(): return sys.stdin.readline().rstrip()


def checkSign(lst):
    cnt = 0
    for i in lst:
        cnt = cnt + 1 if i >= 0 else cnt - 1
    if cnt == -len(lst):
        return -1  # 모두 음수
    elif cnt == len(lst):
        return 1  # 모두 양수
    return 0


n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
prop = 1e10
Flag = checkSign(liquids)
if Flag == -1:  # 모두 음수
    ans = [liquids[-2], liquids[-1]]
if Flag == 1:  # 모두 양수
    ans = [liquids[0], liquids[1]]
elif Flag == 0:
    for i in range(n):
        mn = i + 1
        mx = n - 1
        while mn <= mx:
            mid = (mn + mx) // 2
            new_prop = liquids[i] + liquids[mid]
            if new_prop == 0:
                ans = [liquids[i], liquids[mid]]
                break
            if prop > abs(new_prop):
                ans = [liquids[i], liquids[mid]]
                prop = new_prop
            if new_prop < 0:
                mn = mid + 1
            if new_prop > 0:
                mx = mid - 1
        if prop == 0:
            break
print(ans[0], ans[1])
# [-1000, -99, -40, -10, -1]
# [-1,0,1,2,3,100]
# [-99, -2, -1, 4, 98]
# [-1000, -99, ... ,-50, 0, 1, 13, 21, 98]
# 두 용액을 섞어서 가장 0에 가까운 성분을 가지는 경우를 구해야함.
# 용액의 성질이 모두 같으면 가장 0에 가까운 2개가 정답이다.
# 기준을 무엇으로 잡아야 하는가?
# 최소는 무엇이고 최대는 무엇인가
# 구해야 하는것은 무엇인가? : 두 수의 합이 0에 가까운 두 수
# 0에 가까운...
# 두 수의 합의 최소를 가장 작은 두 수의 합이라고 하고
# 두 수의 합의 최대를 가장 큰 두 수의 합이라고 하자.
# 최소와 최대의 미드 값은 두 수의 합이 될 수 있는 수의 중간값.
# 타겟은 0이라고 하면
# 0보다 크면 mx줄이고 0보다
# 최소를 숫자에서 가장 작은 수라고 하고
# 최대를 숫자에서 가장 큰 수라고 하자
# 그 미드값은
# 2mid가 0에 가까워야함.
# 2mid를 우선 정답으로 저장
# 2mid보다 크면
# 그렇게 하고 두 수의 합을 0으로 가까워지게 한다 ??
# mid값을 정해주고
# 너무 공유기스럽게 풀지말자
# 이 문제는 개수를 구하는 문제가 아니다
#
