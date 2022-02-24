import sys
from collections import deque


def input():
  return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
per = deque([["".join(input().split()), 0]])  # layer의 정보를 같이 저장
ans = "".join(sorted(list(per[0][0])))
if per[0][0] == ans:
  print(0)
  sys.exit()
visited = set()
visited.add(per[0][0])


def BFS():
  while per:
    x, layer = per.popleft()
    for i in range(n - k + 1):
      if i == n - k:
        # reversed -> reverse iterator
        # reversed -> reverseiterator
        y = "".join(list(x[:i]) + list(x[i: i + k])[::-1])
      else:
        y = "".join(list(x[:i]) + list(x[i: i + k])
                    [::-1] + list(x[i + k:]))

      if y in visited:  # 한번 방문한 노드는 다시 만들지 않음.
        continue
      if y == ans:  # 오름차순이 완성되면 반복문 종료
        return layer + 1
      per.append(["".join(y), layer + 1])
      visited.add("".join(y))
  return -1


print(BFS())
