# ----------Title
# 거짓말
# Gold IV
# https://www.acmicpc.net/problem/1043

# ----------Tip
# 진실을 말하는 사람과 같이 있으면 무조건 진실을 말해야함
# 반대로 진실을 들은 사람은 계속 진실을 들어야함

# ----------URLs
#

# ----------Code with Detail
import sys
input = sys.stdin.readline
N, P = map(int, input().split())
T = list(map(int, input().split()))
truth = set()
if len(T) > 1:
  truth |= set(T[1:])
  
infos = []
for p in range(P):
  info = list(map(int, input().split()))
  infos.append(info[1:])
  k = truth & set(info[1:])
  if k:
    truth |= set(info[1:])

ans = 0
for info in infos:
  if not(truth & set(info)):
    ans += 1
print(ans)
