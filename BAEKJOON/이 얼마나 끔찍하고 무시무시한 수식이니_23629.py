# ----------Title
# 이 얼마나 끔찍하고 무시무시한 수식이니
# Gold V
# https://boj.kr/23629

# ----------Tip
# 구현

# ----------URLs

# ----------Code with Detail
import sys
input = sys.stdin.readline


def div(a, b):
  if a < 0:
    a *= -1
    return -(a//b)
  return a//b


def calculate(opr, ans0, a, b):
  if opr == "":
    ans0 = int(a)
  if opr == "+":
    ans0 = int(a) + int(b)
  if opr == "-":
    ans0 = int(a) - int(b)
  if opr == "x":
    ans0 = int(a) * int(b)
  if opr == "/":
    ans0 = div(int(a), int(b))
  return [ans0, ""]


def result(ans0, numbers, ans1):
  minus = ""
  if ans0 < 0:
    minus = "-"
    ans0 *= -1
  elif ans0 == 0:
    sys.stdout.write("ZERO")
    return
  while ans0 > 0:
    ans1 = numbers[ans0 % 10] + ans1
    ans0 //= 10
  sys.stdout.write(minus + ans1)


def check(s: str) -> bool:
  flg = False  # 연산자가 연속해서 나오는 경우 체크
  for i in range(len(s)):
    if s[i] in ["+", "-", "x", "/", "="]:
      if flg:
        return False
      flg = True
      continue
    elif not (48 <= ord(s[i]) <= 57):
      return False
    flg = False
  return True


a, b = "", ""
ans0 = 0
opr = ""


def solve(s, numbers):
  global a, b, ans0, opr
  for i, num in enumerate(numbers):
    s = s.replace(num, str(i))

  if not check(s):
    sys.stdout.write("Madness!")
    return

  sys.stdout.write(s + "\n")

  flg = False
  if s[0] == "-":
    a = "-"
    s = s[1:]
  for i in range(len(s)):
    if s[i] == "=":  # 반례 : THREE=
      a, b = calculate(opr, ans0, a, b)
      result(a, numbers, "")
      return
    if s[i] in ["+", "-", "x", "/"]:
      if flg:
        a, b = calculate(opr, ans0, a, b)
        opr = s[i]
      else:
        opr = s[i]
        flg = True
    elif not flg:
      a += s[i]
    elif flg:
      b += s[i]

  result(a, numbers, "")


if __name__ == "__main__":
  s = input().rstrip()
  numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
             "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
  solve(s, numbers)
