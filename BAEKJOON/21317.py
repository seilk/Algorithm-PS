import sys
input = sys.stdin.readline
n = int(input().rstrip())
enr = [tuple(map(int, input().split())) for i in range(n - 1)]
enr.insert(0, (0, 0))  # dummy
enr.insert(n, (0, 0))
k = int(input().rstrip())
dp = [0 for i in range(n)]  # dummy 포함 (small, big)


def f(n, e, te, flag):
    te += e
    if n == 1:
        return te

    elif n > 1:
        if flag:
            sol = [f(n - 1, enr[n - 1][0], te, True),
                   f(n - 2,  enr[n - 2][1], te, True), f(n - 3, k, te, False)]
            return min(i for i in sol if i > 0)
        else:
            sol = [f(n - 1, enr[n - 1][0], te, False),
                   f(n - 2, enr[n - 2][1], te, False)]
            return min(i for i in sol if i > 0)

    else:
        return 0


print(f(n, 0, 0, True))
