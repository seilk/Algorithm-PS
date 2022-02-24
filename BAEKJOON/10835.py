import sys
input = sys.stdin
n = int(input.readline().rstrip())
left = list(map(int, input.readline().split()))
right = list(map(int, input.readline().split()))
left.insert(0, 0)
right.insert(0, 0)
# 언제든지 왼쪽 카드만 통에 버릴 수도 있고 왼쪽 카드와 오른쪽 카드를 둘 다 통에 버릴 수도 있다. 이때 얻는 점수는 없다.
# 오른쪽 카드에 적힌 수가 왼쪽 카드에 적힌 수보다 작은 경우에는 오른쪽 카드만 통에 버릴 수도 있다. 오른쪽 카드만 버리는 경우에는 오른쪽 카드에 적힌 수만큼 점수를 얻는다.
# (1)과 (2)의 규칙에 따라 게임을 진행하다가 어느 쪽 더미든 남은 카드가 없다면 게임이 끝나며 그때까지 얻은 점수의 합이 최종 점수가 된다.
# 오른쪽 카드를 버릴때만 점수를 얻는다.
# 오른쪽 카드를 버릴 수 있으면 무조건 버린다.
# [3 2 5], [2 4 1]
# 위의 경우에는 오른쪽 2버림 -> 왼쪽만 버림 -> 오른쪽 4버림 -> 오른쪽 1버림 = 7점이 최대이다.
# 오른쪽 카드를 최대한 많이 버리는 쪽으로 작전을 짜야한다.
# 왼쪽에 있는 가장 큰 수 확인하고 그 수가 오른쪽 카드중에서 몇개보다 큰 수인지 확인한다.
# left 더미의 가장 큰 수가 X라고 하자
# right에 X보다 작은 수가 얼마나 있을까?
# 왼쪽에 있는 값보다 큰 오른쪽 값은 점수가 될 수 없다.
# 순서가 중요한 문제
# 왼쪽카드를 행, 오른쪽 카드를 열이라고 하자
# 왼쪽카드를 기준으로 오른쪽 카드에서 점수가 될 수 있는 경우를 체크
<<<<<<< HEAD
<<<<<<< .merge_file_0FqtQb
# modified
=======
>>>>>>> .merge_file_q6ka4r
=======
# modified
>>>>>>> temp2
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if left[i] > right[j - 1]:
            dp[i][j] = max(right[j - 1] + dp[i][j - 1],
                           dp[i - 1][j - 1], dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

if right[n] < left[n]:
    sol = max(dp[n][n] + right[n], dp[n][n])
else:
    sol = dp[n][n]

print(sol)
