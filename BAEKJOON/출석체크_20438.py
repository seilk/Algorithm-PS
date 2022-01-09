#주어지는 TestCase의 개수가 많아서 사전 정리를 잘 해놓아야하는 문제
import sys

input = sys.stdin.readline
N, K, Q, M = map(int, input().split())
students = [1 for i in range(N + 3)]  # ex) N = 4 -> [[0] [1] [2]// [3] [4] [5] [6]]

sleeper = list(map(int, input().split()))
for i in sleeper:
  students[i] = -1

getter = list(map(int, input().split()))
for i in getter:  # 시간복잡도 : O(Q * (N/i))
  if not students[i] == -1:  # sleeper
    for j in range(i, N + 3, i):
      students[j] = 0  # 출석 코드 받은 학생 == 0

for i in sleeper:  # 조는 학생 후 보정
  students[i] = 1

for i in range(4, N + 3):
  students[i] += students[i - 1]

for i in range(M):
  start, end = map(int, input().split())
  if start == 3:
    print(students[end])
  elif students[start] == students[start - 1]:
    print(students[end] - students[start])
  else:
    print(students[end] - students[start] + 1)
