# ----------Title
# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

# ----------Tip
# Heap


# ----------URLs


# ----------Code with Detail
import sys
import heapq


def hot(sc, t):
  for i in sc:
    if i < t:
      return False
  return True


def solution(sc: list, t: int) -> int:
  heapq.heapify(sc)
  ans = 0
  while not hot(sc, t):
    # 원소가 1개면서 target을 넘어가는 경우? : while문의 조건이 target을 넘어가는지에 대한 조건문이기 때문에 원소가 1개면서 통과하는 경우는 더 맵게 만들 수 없는 경우임.
    if len(sc) == 1:
      ans = -1
      break
    x = heapq.heappop(sc)
    y = heapq.heappop(sc)
    heapq.heappush(sc, x + y * 2)
    ans += 1
  return ans


if __name__ == "__main__":
  print(solution([1, 1], 5))
