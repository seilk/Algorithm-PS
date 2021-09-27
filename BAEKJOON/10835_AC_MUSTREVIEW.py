# DP를 재귀함수로 풀면 거의 Top-Down 방식이다.
# Top-Down방식은 보통 dp list가 불필요하다
# 하지만 메모이제이션을 위해서 같이 사용하면 좋다.
# 재귀함수가 무엇을 return을 하는지 잘 확인할 것.
# 새로 호출되는 함수의 return값이 무엇인지 먼저 확인 -> return값이 어떤것을 의미하는지 확인
# 재귀함수라면 return값에 재귀함수 들어가있다. -> 그 재귀함수의 return값이 무엇인지도 같은 순서로 확인.
# 재귀함수 헷갈리면 그냥 return값을 재귀함수에 대입해서 확인한다.
# 재귀함수는 첫 return을 만나기 전까지 계속 들어가므로 그래프 그릴 때 여기저기 분산해서 그리지 말것
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input().rstrip())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[-1 for i in range(n)] for i in range(n)]
# dp라는 list는 메모를 해서 시간 절약을 도와주는 용도인데 0으로 초기화했다가 0 자체가 값이 되는 경우에는 시간 절약이 안됨.


def f(l, r):
    if l >= n or r >= n:
        return 0
    # 메모이제이션, dp가 0이상의 값이 이미 존재하면 바로 return, 이미 다른 재귀함수에서 구했으므로 그냥 가져다 쓰면 됨. 또 새끼치면서 재귀함수 돌 이유 없음.(시간낭비임)
    if dp[l][r] >= 0:
        return dp[l][r]

    # 현재 위치한 곳의 값이 오른쪽 카드가 더 작을 때는 무조건 더하는게 높은 값을 갖는 경우임.
    if right[r] < left[l]:
        # 재귀함수를 돌면서 똑같은 값 처리를 위한 메모
        # 함수를 한번 더 들어가고 그 값에 오른쪽 카드 값을 더한다.
        dp[l][r] = f(l, r + 1) + right[r]
    else:
        dp[l][r] = max(f(l + 1, r), f(l + 1, r + 1))  # 왼쪽 먼저 재귀 들어감.

    return dp[l][r]  # 함수들은 현재 위치의 dp값을 리턴한다.


f(0, 0)
print(dp[0][0])
