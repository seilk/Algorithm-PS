import sys


def isprime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  elif n > 2:
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True


def find(tg):
  for i in range(len(prime) - 1):
    n = prime[i] * prime[i + 1]
    if tg < n:
      return n


if __name__ == "__main__":
  input = sys.stdin.readline
  num = int(input().rstrip())
  prime = []
  for k in range(104):
    if isprime(k):
      prime.append(k)
  print(find(num))
