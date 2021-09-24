import sys
n = int(sys.stdin.readline().rstrip())
lst = []
if n > 1:
    while n != 1:
        lst.append(n % 2)
        n //= 2
    lst.reverse()
    lst.insert(0, n)
    print(*lst, sep = "")
else:
    print(1)
