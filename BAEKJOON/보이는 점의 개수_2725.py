import sys
def input(): return sys.stdin.readline().rstrip()
# n은 거리를 의미함. 따라서 n = 2 -> 점의 개수 3임.


def tangent(x, y):
    if x == 0:
        return "inf"
    return y / x


cases = int(input())
# 보이지 않는 점은 "기울기"가 겹치는 점임!
# 기울기 아이디어 꼭 기억할 것!
# dp에 미리 보이는 점의 개수를 저장(memoization)해두고 dp[n]에서는 dp[n - 1]의 값에 테두리 점만 반복하게 함.
# 테두리도 절반만 반복하고 *2 처리함. -> 정사각형이라 y = x에 대칭임.
# 겹치는 기울기는 set을 이용해서
dp = [0 for i in range(1001)]
dp[1] = 3
t_set = {0, "inf", 1}
for i in range(2, 1001):
    t_set_sub = set()
    x = i
    for y in range(0, i):
        t_set_sub.add(tangent(x, y))
    dp[i] = dp[i - 1] + 2 * (len(t_set_sub - t_set))
    t_set |= t_set_sub

for i in range(cases):
    print(dp[int(input())])
