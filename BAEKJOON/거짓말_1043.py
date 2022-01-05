# ----------Title
# 거짓말
# Gold IV
# https://www.acmicpc.net/problem/1043

# ----------Tip
# 진실을 말하는 사람과 같이 있으면 무조건 진실을 말해야함
# 반대로 진실을 들은 사람은 계속 진실을 들어야함
# 진실만을 말해야 하는 사람의 root = -1

# ----------URLs
# https://www.acmicpc.net/board/view/72203
#
#
# ----------Code with Detail
import sys
input = sys.stdin.readline
N, P = map(int, input().split())
T = list(map(int, input().split()))  # 초기 진실리스트
truth = [i for i in range(N + 1)]  # 루트 노드를 저장
if len(T) > 1:
  for t in T[1:]:
    truth[t] = -1


def find(n):
  if truth[n] < 0:
    return truth[n]
  elif truth[n] == n:
    return n
  else:
    truth[n] = find(truth[n])
    return truth[n]


def union(n, m):
  a = find(n)
  b = find(m)
  if a == b:
    return
  # 숫자의 크기가 더 작은 쪽으로 묶음
  elif a < b:
    truth[b] = a
  elif b < a:
    truth[a] = b


infos = []
for p in range(P):
  info = list(map(int, input().split()))  # 매 파티마다 참석하는 사람들의 info
  infos.append(info[1:])
  for i in info[1:]:  # 거짓인 기준 노드 찾기
    if find(i) != -1:
      std = i
      break
  for i in info[1:]:
    if find(i) == -1:  # 진실인이 한 명이라도 있으면 std 바꾸고 모두 union
      std = i
      for j in info[1:]:
        union(std, j)
      break
    else:
      union(std, i)  # 거짓인은 기준노드로 묶음 (한명이 진실인으로 바뀌면 같이 바뀌도록)


ans = 0
for info in infos:
  flg = True
  for i in info:
    if find(i) < 0:
      flg = False
      break
  if flg:
    ans += 1
print(ans)
