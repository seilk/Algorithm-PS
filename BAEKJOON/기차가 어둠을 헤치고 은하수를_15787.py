# ----------Title
# 기차가 어둠을 헤치고 은하수를
# Silver II
# https://boj.kr/15787

# ----------Tip
# BitMask
# toggle 부분 2가지 방법 숙지(not and toggle, xor toggle)
# XOR vs ~()

# ----------URLs

# ----------Code with Detail
import sys
def input(): return sys.stdin.readline().rstrip()


t, c = map(int, input().split())
trains = [0] * (t + 1)  # t개의 기차 (index 맞춤)
commands = [list(map(int, input().split())) for i in range(c)]  # commands


def ride(nt, seat):
  if not (trains[nt] & (1 << seat)):
    trains[nt] |= 1 << seat  # or


def leave(nt, seat):
  if (trains[nt] & (1 << seat)):
    trains[nt] ^= (1 << seat)  # toggle


def back(nt):
  # trains[nt] = trains[nt] << 1
  # trains[nt] &= (1 << 21) - 1  # 하차(toggle), if 필요없음
  if trains[nt] & (1 << 20):
    trains[nt] ^= 1 << 20  # toggle
  trains[nt] = trains[nt] << 1


def forward(nt):
  # trains[nt] = trains[nt] >> 1
  # trains[nt] &= ~1  # 하차(toggle), if 필요없음
  if trains[nt] & 2:
    trains[nt] ^= 2
  trains[nt] = trains[nt] >> 1


for co in commands:
  if co[0] == 1:
    ride(co[1], co[2])
  if co[0] == 2:
    leave(co[1], co[2])
  if co[0] == 3:
    back(co[1])
  if co[0] == 4:
    forward(co[1])
milkyway = set(trains[1:])
print(len(milkyway))

a = 0b11101  # 10101
print(bin(a))
a &= ~(1 << 1)
print(bin(a))

b = 0b11101  # 10101
print(bin(b))
if (b & 1 << 1):
  b ^= (1 << 1)
print(bin(b))

print(a == b)
# 1 2
# 1 1 20
# 3 1

if not 0:
  print("zero is false")

lst = [1, 2, 3]
lst.remove(0)
