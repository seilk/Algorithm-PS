from sys import stdin
from collections import defaultdict as dfd
input = stdin.readline


def isSuprise(s, p):
  k = dfd(int)
  l = len(s)
  for i in range(l-(p+1)):
    ns = s[i] + s[i + p + 1]
    if k[ns] == 0:
      k[ns] += 1
    else:
      return False
  return True


if __name__ == "__main__":
  while 1:
    strng = input().rstrip()
    flg = True
    if strng == "*":
      break
    for p in range(len(strng)-1):
      if not (isSuprise(strng, p)):
        print(strng + " is NOT surprising.")
        flg = False
        break
    if flg:
      print(strng + " is surprising.")
