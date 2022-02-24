import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n, 1, -1):
    print(' ' * (n - i) + ('*' * (2 * i - 1)));
print( ' ' * (n - 1) + '*')
for j in range(2, n + 1):
    print(' ' * (n - j) + ('*' * (2 * j - 1)));
