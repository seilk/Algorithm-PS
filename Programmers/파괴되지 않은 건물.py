def solution(board, skill):
  N = len(board)
  M = len(board[0])
  PREFIX_BOARD = [[0] * (M + 1) for i in range(N + 1)]

  for query in skill:
    type, r1, c1, r2, c2, degree = query
    if type == 1:
      degree *= -1
    PREFIX_BOARD[r1][c1] += degree
    PREFIX_BOARD[r1][c2 + 1] += -degree
    PREFIX_BOARD[r2 + 1][c1] += -degree
    PREFIX_BOARD[r2 + 1][c2 + 1] += degree


  for i in range(N):
    for j in range(1, M + 1):
      PREFIX_BOARD[i][j] += PREFIX_BOARD[i][j - 1]

  for j in range(M):
    for i in range(1, N + 1):
      PREFIX_BOARD[i][j] += PREFIX_BOARD[i - 1][j]

  ans = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] + PREFIX_BOARD[i][j] > 0:
        ans += 1
  return ans

solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
         [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])
