import sys
def input(): return sys.stdin.readline().rstrip()


want, cities = map(int, input().split())
infos = [list(map(int, input().split())) for i in range(cities)]
dp = [100_000] * 1001  # 최대 원하는 고객 수 * 최대 비용(모든 호텔이 [1, 100] 인 상황)
dp[0], dp[1] = 0, min(infos, key=lambda x: x[0])[0]
for people in range(2, want + 1):
    for info in infos:
        prev = people - info[1]
        if prev <= 0:
            prev = 0
        # dp[people] = 호텔마다 돌아다니면서 현재 people에서 추가할 수 있는 사람의 수를 빼준 상황에서의 dp값(최소 가격)
        dp[people] = min(dp[people], dp[prev] + info[0])

print(dp[want])
