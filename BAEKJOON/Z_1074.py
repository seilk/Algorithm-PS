import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()


N, r, c = map(int, input().split())
rowL = [0, int(2**(N) / 2), 2**(N)]
colL = [0, int(2**(N) / 2), 2**(N)]


def fractal(rowL, colL, N, v):
    global r
    global c
    if N == 0:
        return int(v)

    if rowL[0] <= r < rowL[1]:
        rowL = [rowL[0], int((rowL[0] + rowL[1]) / 2), rowL[1]]
        if colL[0] <= c < colL[1]:  # coord = 1
            colL = [colL[0], int((colL[0] + colL[1]) / 2), colL[1]]
            v += 0 * (2**(2 * N)) / 4

        elif colL[1] <= c < colL[2]:  # coord = 2
            colL = [colL[1], int((colL[1] + colL[2]) / 2), colL[2]]
            v += 1 * (2**(2 * N)) / 4

    elif rowL[1] <= r < rowL[2]:  # coord = 1
        rowL = [rowL[1], int((rowL[1] + rowL[2]) / 2), rowL[2]]
        if colL[0] <= c < colL[1]:
            colL = [colL[0], int((colL[0] + colL[1]) / 2), colL[1]]
            v += 2 * (2**(2 * N)) / 4

        elif colL[1] <= c < colL[2]:  # coord = 2
            colL = [colL[1], int((colL[1] + colL[2]) / 2), colL[2]]
            v += 3 * (2**(2 * N)) / 4

    return fractal(rowL, colL, N - 1, v)


print(fractal(rowL, colL, N, 0))

# 처음 사각형의 1/4등분에 포함되는 숫자 : 2**(2*N) / 4 개
# 각 포지션을 알아두면 된다.
# 누적합.
