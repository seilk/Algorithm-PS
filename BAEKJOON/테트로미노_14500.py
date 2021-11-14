import sys
def input(): return sys.stdin.readline().rstrip()


rowsize, colsize = map(int, input().split())
field = [list(map(int, input().split())) for i in range(rowsize)]
direction1 = [[[[1, 0], [0, 1], [1, 1]]]]  # ㅁ 모양
#
direction2 = [[[[0, 1], [0, 2], [0, 3]],  # ㅡ모양
               [[1, 0], [2, 0], [3, 0]]]]
#
direction3 = [[[[0, -1], [1, -1], [2, -1]],  # ㄴ모양
               [[0, -1], [-1, -1], [-2, -1]],
               [[0, 1], [1, 1], [2, 1]],
               [[0, 1], [-1, 1], [-2, 1]],
               [[-1, 0], [-1, 1], [-1, 2]],
               [[1, 0], [1, 1], [1, 2]],
               [[1, 0], [1, -1], [1, -2]],
               [[-1, 0], [-1, -1], [-1, -2]]]]
#
direction4 = [[[[-1, 0], [-1, -1], [-2, -1]],  # ㄹ모양
               [[0, 1], [-1, 1], [-1, 2]],
               [[-1, 0], [-1, 1], [-2, 1]],
               [[0, -1], [-1, -1], [-1, -2]]]]
#
direction5 = [[[[-1, 0], [-1, -1], [-1, 1]],  # ㅓ모양
               [[0, -1], [1, -1], [-1, -1]],
               [[1, 0], [1, -1], [1, 1]],
               [[0, 1], [1, 1], [-1, 1]]]]
#

directions = direction1 + direction2 + direction3 + direction4 + direction5


def check(coords, i, j):
    if not (0 <= i + coords[0][0] < rowsize):
        return False
    if not (0 <= j + coords[0][1] < colsize):
        return False
    if not (0 <= i + coords[1][0] < rowsize):
        return False
    if not (0 <= j + coords[1][1] < colsize):
        return False
    if not (0 <= i + coords[2][0] < rowsize):
        return False
    if not (0 <= j + coords[2][1] < colsize):
        return False
    return True


ans = 0
for i in range(rowsize):
    for j in range(colsize):
        for direction in directions:  # 5개의 direction
            for coords in direction:  # 4~8방향의 coords
                tot = field[i][j]
                if check(coords, i, j):
                    tot += field[i + coords[0][0]][j + coords[0][1]]
                    tot += field[i + coords[1][0]][j + coords[1][1]]
                    tot += field[i + coords[2][0]][j + coords[2][1]]
                ans = max(tot, ans)
print(ans)
