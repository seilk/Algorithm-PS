def solution(n, info):
  apeach = 0
  mxx = (0, [0] * 11)
  for i in range(2048):  # i = 0 ~ 2047 ex) i == 2030
    rr = [0] * 11 # 라이언이 이기는 경우 001..000
    for bt in range(11, -1, -1):
      if 2 ** bt & i:
        rr[10 - bt] = 1
    rrr = [0] * 11
    arrow = 0
    scoreAP = 0
    scoreRY = 0
    for idx in range(11):
      if idx == 10 and arrow < n:
        rrr[idx] = n - arrow
        arrow = n
        continue
      if rr[idx] == 1 and info[idx] > 0:  # 어피치가 화살을 쏜 라운드에서 라이언이 이기는 경우
        arrow += info[idx] + 1  # 라이언이 쏜 전체 화살 수
        rrr[idx] += info[idx] + 1  # 해당 점수에서의 화살 수
        scoreRY += 10 - idx  # 라이언의 점수
      elif rr[idx] == 0 and info[idx] > 0:  # 어피치가 쏜 라운드에서 어피치가 이기는 경우
        scoreAP += 10 - idx  # 어피치의 점수
      elif rr[idx] == 1 and info[idx] == 0:  # 어피치가 쏘지 않은 라운드에서 라이언이 이기는 경우
        scoreRY += 10 - idx
        rrr[idx] += info[idx] + 1
        arrow += 1

    if arrow == n and scoreRY > scoreAP:
      diff = scoreRY - scoreAP
      if mxx[0] < diff:
        mxx = diff
        mxx = (diff, rrr)
      elif mxx[0] == diff:
        flg = False
        for k in range(10, -1, -1):
          if mxx[1][k] < rrr[k]:
            flg = True
            break
          elif mxx[1][k] > rrr[k]:
            flg = False
            break
        if flg:
          mxx = (diff, rrr)
  if mxx[1] == [0] * 11:
    return [-1]
  return mxx[1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
