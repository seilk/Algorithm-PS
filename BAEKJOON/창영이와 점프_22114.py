import sys
def input(): return sys.stdin.readline().rstrip()


n, e = map(int, input().split())
diffs = list(map(int, input().split()))

ans, cnt, chance = 2, 1, False
i, pre = 0, 0
while i < n - 1:
    if diffs[i] > e and chance:
        chance = False
        ans = max(ans, cnt)
        cnt = 1
        i = pre
        continue
    if diffs[i] > e and (not chance):
        chance = True
        pre = i + 1
    cnt += 1
    i += 1
#
if cnt > ans:
    ans = cnt
print(ans)

# diff가 e를 넘으면 건널 수 없음
# e를 넘는 수 하나를 포함하면서 최대 길이를 구하면 됨.
# 정렬은 아님
# n이 10만개
# 조건을 만족하는 diff의 개수가 6이라면 answer은 7
# e보다 큰 수를 base camp라고 생각하고 첫번째 블럭에서 첫번째 base camp를 찬스로 지나고 두번째 base camp까지 합계, 첫번째 base camp 다음 블럭에서 두번째 base camp를 지나 세번째 base camp까지의 합계 중에서 최대를 뽑으면됨. O(N)

ㅇ ㅇ X ㅇ ㅇ ㅇ X ㅇ ㅇ
