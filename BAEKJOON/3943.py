import sys
def f():
    return int(sys.stdin.readline().rstrip())
t = f()
lst = []

for i in range(t):
    n = f()
    lst.append(n)
    while 1 not in lst:
        if n % 2 == 0:
            n /= 2 
            lst.append(n)
        else:
            n = n * 3 + 1
            lst.append(n)
    print(int(max(lst))); lst = []