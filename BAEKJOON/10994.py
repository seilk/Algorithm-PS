n = int(input())
m = 4 * n - 3
plate = [[" " for _ in range(m)] for _ in range(m)]


def star(n, x, y):
    m = 4 * n - 3
    if n == 1:
        plate[x][y] = "*"
        return
    for i in range(m):
        plate[x][y + i] = "*"
        plate[x + i][y] = "*"
        plate[x + m - 1][y + i] = "*"
        plate[x + i][y + m - 1] = "*"
    return star(n - 1, x + 2, y + 2)


star(n, 0, 0)
for _ in range(m):
    print(*plate[_], sep="")
