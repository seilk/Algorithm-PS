import sys
def input(): return sys.stdin.readline().rstrip()


n, c = map(int, input().split())
coord = [int(input()) for i in range(n)]
coord.sort()

mn, mx = 1, coord[-1] - coord[0]
answer = 1

while mn <= mx:  # mn과 mx가 같은 상황도 봐야함.
  standard = 0  # 첫번째 집의 좌표
  mid = (mn + mx) // 2
  cnt = 1
  for i in range(1, n):
    if coord[i] - coord[standard] >= mid:  # 정해준 간격이상일때 공유기 심기.
      # 가장 인접한 간격 = mid (공유기 간의 최소간격)
      # 이 간격을 가장 크게 만들어야 함.
      cnt += 1  # 10 -> 9
      standard = i
  # 실제로 설치한 공유기의 개수 = cnt
  # 목표 설치 대수 = c
  if cnt > c:  # 공유기를 더 큰 간격으로 설치할 수 있을 때 : 간격 늘리기
    answer = max(mid, answer)
    mn = mid + 1
    # 반례 ???
    # 1 2 3 5 7 9 11
  if cnt == c:  # 공유기 갯수에 맞게끔 간격을 유지해도 그 간격보다 크게 공유기를 심을 수 있는지 확인해야함 -> 간격을 넓혀야함
    answer = max(mid, answer)
    mn = mid + 1
  if cnt < c:  # 간격을 좁혀야 함.
    mx = mid - 1
print(answer)

##WRONG_ANSWER##
# 이 코드는 인접한 두 공유기의 거리를 구하기보다는 공유기를 심는 simulation에 가까움
# 그리고 잘못된 가정도 섞여있음
# 문제에서 구해야 하는 것은 두 공유기의 최대거리
# 따라서 가능한 공유기 사이 거리를 먼저 최소=left, 최대=right로 구하고 이진탐색으로 공유기 거리를 줄이면서 문제 조건에 맞는 공유기 거리를 구해야한다.
# right, left = len(coord) - 1, 0
# c -= 2
# tmp = coord[right] - coord[left]
# maxwhat = [[-1, tmp]]
# while c > 0:
#     pre_left = left
#     pre_right = right
#     minwhat = []
#     while right - left > 1:
#         mid = (right + left) // 2
#         gap_right, gap_left = coord[pre_right] - \
#             coord[mid], coord[mid] - coord[pre_left]
#         if gap_right >= gap_left:
#             left = mid
#         else:
#             right = mid
#         minwhat.append([mid, min(gap_left, gap_right)])
#     if minwhat:
#         maxwhat.append(max(minwhat, key=lambda x: x[1]))
#     else:
#         maxwhat.append([(left + right) // 2, 1])
#     mid = maxwhat[-1][0]
#     if (mid - pre_left) > (pre_right - mid):
#         right = mid
#         left = pre_left
#     else:
#         left = mid
#         right = pre_right
#     c -= 1

# print(min(maxwhat, key=lambda x: x[1])[1])
