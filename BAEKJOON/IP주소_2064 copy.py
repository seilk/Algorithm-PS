#WRONG ANSWER
# ----------Title
# IP주소
# Gold III
# https://boj.kr/2064

# ----------Tip
# 비트마스킹
# 논리연산
# 기초 CS 지식

# ----------URLs

# ----------Code with Detail
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
ips = [list(map(int, input().split(sep=".")))
       for i in range(n)]  # 1000개의 주소 저장, 각각의 바이트 idx로 접근 [0...3]
flg = 0
for idx in range(4):  # 다른 바이트 찾기
  tmp = ips[0][idx]  # ips[0][0]을 기준으로 삼음
  for ip in ips:
    if tmp != ip[idx]:
      flg = 1
      break
  if flg:
    break

std = [0] * 8
for i in range(7, -1, -1):  # 왼쪽에서 오른쪽으로 검색
  std[i] = ips[0][idx] & (2 ** i)

flgg = 0
for t in range(7, -1, -1):
  for i in range(1, n):
    if (ips[i][idx] & (2 ** t)) == std[t]:
      continue
    else:
      flgg = 1
      break
  if flgg:
    break

address = [0, 0, 0, 0]
mask = [0, 0, 0, 0]
for i in range(0, idx):  # mask의 idx - 1까지
  mask[i] = 255
if 0 <= t < 7:  # mask의 idx 부분
  mask[idx] = ((1 << 8) - 1) ^ ((1 << (t + 1)) - 1)
  #11111111 ^ 00111111 = 11000000 = 128 + 64 = 192
elif t == 7:
  mask[idx] = 0


for i in range(4):
  address[i] = ips[0][i] & mask[i]

print(*address, sep=".")
print(*mask, sep=".")
