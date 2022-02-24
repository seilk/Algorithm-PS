# BOJ_14226 이모티콘
# 0.화면에 이모티콘 1개 출력되어있음.
# 1.화면의 모든 이모티콘을 클립보드에 복사 (이전 클립보드는 삭제됨)
# 2.클립보드의 이모티콘을 붙여넣기
# 3.화면 이모티콘을 하나 삭제
import sys
def input(): return sys.stdin.readline().rstrip()


def solution(s):
  # 모든 i는 i+1에 영향을 받음 -> 1001까지 먼저 계산하는게 좋음
  # cached[나누어 지는 수] = min(몫 + cache[n] , cache[n], cache[n + 1] + 1)
  for i in range(1, 1002):  # i = 1 i = 2 i = 3
    for j in range(2, 1002):  # x1은 이미 초기화 해준 상태이므로 제외
      if i * j <= 1001:  # 1, 19
        cache[i * j] = min(cache[i] + j, cache[j * i])
    # 뒤에서 부터 처리해줘야함. cache[n]의 최소값에 cache[n + 1] + 1이 들어가기 때문
    for k in range(1000, 1, -1):
      cache[k] = min(cache[k], cache[k + 1] + 1)
  print(cache)
  print(cache[s])


s = int(input())
time, clipboard, cur = 0, 0, 1
cache = [i for i in range(1002)]  # s == 3 : [0, c[1], c[2], c[3], c[4]]
cache[1] = 0
cache[2] = 2
solution(s)

# 1 -> 복 -> 붙 : n : n sec
# cache[2] = 2
# cache[3] = 3
# cache[4] = 4
# cache[5] = 5
# cache[6] = 5
# cache[7] = 7
# cache[8] = 6
# cache[9] = 6
# cache[10] = 7
# cache[11] = ??
# 11 -> 11 : 8/ 12 - 1


# 이모티콘 3개 만드는 방법 경우의 수
#1 > copy > paste > paste (3)
# 어떤 이모티콘이든 아무리 느려도 s의 시간만큼은 걸림(1개를 단순 복붙)
# s보다 짧으면 그건 방법의 경우
# 1 > cp > pst > pst > cp > pst (t = 5)
# 6개의 이모티콘의 경우 3개에서 cp하고 pst하면 더 짧은 시간에 가능
# 1 > cp > pst > pst > pst > pst (t = 5)
# cache[18] = 6개 만든 상황에서 3번 pst하면 됨
# 1 > cp > pst > pst > cp > pst > cp > pst > pst (t = 8)
# n보다 작은 수중에서 2이상으로 나누어 떨어지는 수를 몫만큼 cp and paste
# 홀수는 1부터 연속으로 pst하는 경우와 n + 1을 만드는 시간의 +1 한 것을 비교