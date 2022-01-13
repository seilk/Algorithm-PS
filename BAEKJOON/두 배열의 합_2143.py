import sys


def makePartialSum():
  global i
  for i in range(N):
    sumlistx.append(listx[i])
    psum = listx[i]
    for j in range(i + 1, N):
      psum += listx[j]
      sumlistx.append(psum)
  for i in range(M):
    sumlisty.append(listy[i])
    psum = listy[i]
    for j in range(i + 1, M):
      psum += listy[j]
      sumlisty.append(psum)


def checkSameValue(end):
  global ans
  cnt = 0
  for j in range(end, len(sumlisty)):
    if sumlisty[j] != sumlisty[end]:
      break
    else:
      cnt += 1
  ans += cnt
  return (tagx, cnt)


def checkLowerBoundOfListy():
  start = 0
  end = len(sumlisty) - 1
  while start < end:  # lowerbound
    mid = (start + end) // 2
    if tagx + sumlisty[mid] < T:
      start = mid + 1
    elif tagx + sumlisty[mid] >= T:
      end = mid
  return end


def setInit():
  global T, N, listx, M, listy, sumlistx, sumlisty
  T = int(input().rstrip())
  N = int(input().rstrip())
  listx = list(map(int, input().split()))
  M = int(input().rstrip())
  listy = list(map(int, input().split()))
  sumlistx = []
  sumlisty = []


def solve():
  global ans, i, tagx
  ans = 0
  pre = (None, None)
  for i in range(len(sumlistx)): #A를 기준리스트
    tagx = sumlistx[i]
    if pre[0] == tagx:
      ans += pre[1]
      continue
    end = checkLowerBoundOfListy()
    if tagx + sumlisty[end] == T:
      pre = checkSameValue(end)


if __name__ == "__main__":
  input = sys.stdin.readline
  # 초기값 세팅
  setInit()
  # 두 리스트의 모든 부분합 구하고 정렬, 부분합을 하나의 item으로 보는 관점
  makePartialSum()
  sumlistx.sort()
  sumlisty.sort()
  # 기준 리스트를 listx로 잡고 NlogM으로 이분탐색!
  solve()
  print(ans)
