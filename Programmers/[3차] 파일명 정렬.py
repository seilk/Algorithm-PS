import sys

input = sys.stdin.readline


def solution(files):
  # head, number, tail 구분
  tmp = []
  seperate(files, tmp)
  sort_file(tmp)
  ans = []
  for i in range(len(tmp)):
    ans.append("".join(tmp[i][:-1]))
  return ans


def sort_file(tmp):
  for i in range(len(tmp)):
    tmp[i]
    for j in range(i, len(tmp)):
      if tmp[i][0].casefold() > tmp[j][0].casefold():
        swap(i, j, tmp)
        continue
      elif tmp[i][0].casefold() == tmp[j][0].casefold() and int(tmp[i][1]) > int(tmp[j][1]):
        swap(i, j, tmp)
        continue
      elif tmp[i][0].casefold() == tmp[j][0].casefold() and int(tmp[i][1]) == int(tmp[j][1]) and tmp[i][3] > tmp[j][3]:
        swap(i, j, tmp)


def swap(i, j, tmp):
  boo = [tmp[i][0], tmp[i][1], tmp[i][2], tmp[i][3]]
  tmp[i] = [tmp[j][0], tmp[j][1], tmp[j][2], tmp[j][3]]
  tmp[j] = [boo[0], boo[1], boo[2], boo[3]]


def seperate(files, tmp):
  for file in files:
    frm = 0
    tto = 0
    flg = False
    for x in range(len(file)):
      if flg == False and 48 <= ord(file[x]) <= 57:
        frm = x  # number 부분의 시작점
        flg = True
      if flg == True and not (48 <= ord(file[x]) <= 57):
        tto = x
        break
      elif flg == True and x == len(file) - 1:
        tto = x + 1
        break
    tmp.append([file[:frm], file[frm:tto], file[tto:]])  # head, number, tail
  # 입력 순위 추가해주기
  for i in range(len(tmp)):
    tmp[i].append(i)


# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
solution(["F-15"])
