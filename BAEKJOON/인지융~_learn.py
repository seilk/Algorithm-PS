n = int(input())
a, b = map(int, input().split())
orga, orgb = a, b
board = [[0] * n for __ in range(n)]
for i in range(n*2-1):
    if a <= 0: break
    for r in range(max(0, i - n + 1), min(n, i + 1)):
        if a <= 0: break
        c = i - r
        board[r][c] = 1
        a -= 1

        # assert 0 <= r < n > c >= 0
        # assert 0 <= i - r < n
        # assert -i <= - r < n - i
        # assert i - n < r <= i
        # assert i - n + 1 <= r < i + 1

for i in range(n*2-1):
    if b <= 0: break
    for r in range(max(0, i - n + 1), min(n, i + 1)):
        if b <= 0: break
        c = i - r
        board[~r][~c] = 2
        b -= 1

        # assert 0 <= r < n > c >= 0
        # assert 0 <= i - r < n
        # assert -i <= - r < n - i
        # assert i - n < r <= i
        # assert i - n + 1 <= r < i + 1

success = True
if sum(rw.count(1) for rw in board) != orga:
    success = False
if sum(rw.count(2) for rw in board) != orgb:
    success = False
if any(board[r][c] + board[r+1][c] == 3 for r in range(n - 1) for c in range(n)):
    success = False
if any(board[r][c] + board[r][c+1] == 3 for r in range(n) for c in range(n - 1)):
    success = False
if success:
    print(1)
    for rw in board: print(*rw, sep='')
else:
    print(-1)