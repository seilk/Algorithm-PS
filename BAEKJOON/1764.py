# set에 저장하고 set에 있으면 따로 빼는식으로 정렬
from sys import stdin
n, m = map(int, stdin.readline().split())
people = set()  # {a} <- a =========> {a}
neither = []

# 듣도보도 못한 사람은
# 듣도 못한 사람의 수 < 보도 못한 사람의 수
# 듣도 보도 못한 사람은 듣도 못한 사람에 전부 포함된다.

for i in range(n):
<<<<<<< HEAD
  people.add(str(stdin.readline().rstrip()))

for i in range(m):
  p = str(stdin.readline().rstrip())
  if p in people:
    neither.append(p)
=======
    people.add(str(stdin.readline().rstrip()))

for i in range(m):
    p = str(stdin.readline().rstrip())
    if p in people:
        neither.append(p)
>>>>>>> temp2

neither.sort()
print(len(neither))
print(*neither, sep='\n')
