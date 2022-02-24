from sys import stdin

n, k = map(int, stdin.readline().split())
lst = [i for i in range(1, n + 1)]  # [0, 1, 2, 3, 4, ... , n]
sol = []
while len(lst) > 1:
    x = (k - 1) % len(lst)
    lst = lst[x + 1 :] + lst[: x + 1]
    sol.append(lst.pop())
sol.append(lst[0])
print("<", end="")
print(*sol, sep=", ", end="")
print(">")
