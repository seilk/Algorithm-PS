# ----------Title
# 톱니바퀴
# Gold V
# https://boj.kr/14891

# ----------Tip
# Simulation
# BitMask
# BitMask Little Mistake :(
# Logic Operator
# BitMasking으로 문제 풀 때 단순 Literal "1"을 비교하는지 "128"을 비교하는지 고려하고 적절히 Shift할 것
# index fitting 실수조심
# 톱니가 돌아가고 나서의 비교가 아닌 돌아가기 전의 상황을 비교해야함

# ----------URLs


# ----------Code with Detail
import sys
sys.setrecursionlimit(10 ** 7)


def checkleft(d, i, x, ts):
  if i == 0:  # 왼쪽의 마지막
    return
  if x == (ts[i] & 32) >> 5:  # 극이 같을때
    return
  x = (ts[i] & 2) >> 1
  # 회전
  if d > 0:
    rr = (ts[i] & 1) << 7
    ts[i] = (ts[i] >> 1) | rr  # 시계방향 회전
  else:
    ll = (ts[i] & 128) >> 7
    ts[i] = (ts[i] << 1) | ll  # 반시계방향 회전

  # 재귀적으로 왼쪽 톱니 회전 판단
  checkleft(-d, i - 1, x, ts)
  return


def checkright(d, i, y, ts):
  if i == 5:  # 오른쪽의 마지막
    return
  if y == (ts[i] & 2) >> 1:  # 극이 같을때
    return
  y = (ts[i] & 32) >> 5

  # 회전
  if d > 0:
    rr = (ts[i] & 1) << 7
    ts[i] = (ts[i] >> 1) | rr
  else:
    ll = (ts[i] & 128) >> 7
    ts[i] = (ts[i] << 1) | ll

  # 재귀적으로 오른쪽 톱니 회전 판단
  checkright(-d, i + 1, y, ts)
  return


def rotate(d, i, ts):
  # 회전여부 판단
  x = (ts[i] & 2) >> 1  # left 인자
  y = (ts[i] & 32) >> 5  # right 인자
  # 톱니 갱신
  if d > 0:
    rr = (ts[i] & 1) << 7
    ts[i] = (ts[i] >> 1) | rr
  else:
    ll = (ts[i] & 128) >> 7
    ts[i] = (ts[i] << 1) | ll

  checkleft(-d, i - 1, x, ts)  # (반대방향 회전, 왼쪽 인덱스, 6번째 톱니 상태, 톱니SET)
  checkright(-d, i + 1, y, ts)  # (반대방향 회전, 오른쪽 인덱스, 2번째 톱니 상태, 톱니SET)
  return


def point(ts):
  ans = 0
  for i in range(1, 5):
    ans += (2 ** (i - 1)) * ((ts[i] & 128) >> 7)
  sys.stdout.write(str(ans) + "\n")
  return


if __name__ == "__main__":
  input = sys.stdin.readline
  ts = [0] + [int(input(), 2) for i in range(4)]  # 입력을 bit로 생각하고 int로 저장
  r = int(input())  # command 횟수
  rs = [tuple(map(int, input().split()))
        for i in range(r)]  # command => (톱니바퀴 번호, direction)
  for i, d in rs:  # 톱니바퀴 번호, 방향
    rotate(d, i, ts)  # rotate(방향, 톱니번호, 톱니set)

  # point 계산
  point(ts)

# print((0b00000000 & (1 << 6)) >> 6)
