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
ip = [0] * n
for i in range(n):
  for j in range(4):
    ip[i] <<= 8  # 왼쪽으로 밀어주면서 뒤에 채워넣어주는 상황
    ip[i] |= ips[i][j]

flg = 0
mask = 0
for i in range(31, -1, -1):  # 1<<31 = 32번째 숫자만 1인 비트
  bit = 1 << i
  for j in range(1, n):
    if (ip[0] & bit) != (ip[j] & bit):
      flg = 1
      break
  if flg:
    break
  mask |= bit
address = ip[0] & mask


def printt(n):
  # 오른쪽으로 밀었을 때(>>) 자리수를 넘어가는 숫자는 그냥 사라지는 취급
  return [(n >> 24) & (255), (n >> 16) & (255), (n >> 8) & (255), n & 255]


print(*printt(address), sep=".")
print(*printt(mask), sep=".")
