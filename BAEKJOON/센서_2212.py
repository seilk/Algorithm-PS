# ----------Title
# 센서
# Gold V
# https://boj.kr/2212

# ----------Tip
# Greedy
# Greedy는 문제 이해가 핵심이다.
# 문제 이해가 어려웠던 문제
# <<행복유치원>>과 동일한 문제

# ----------URLs

# ----------Code with Detail
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
k = int(input())
highway = list(map(int, input().split()))
highway.sort()
diff = [highway[i] - highway[i - 1] for i in range(1, n)]
diff_slice = sorted(diff, reverse=True)[:k - 1]
print(sum(diff) - sum(diff_slice))

# 1 3 6 6 7 9
# 2 3 0 1 2
