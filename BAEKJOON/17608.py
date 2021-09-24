import sys
n = int(sys.stdin.readline())  #막대기의 개수
# dp = [0 for _ in range(n + 1)]  # [0, 0, 0, 0, 0, ...]
lst = []
# dp = []
for i in range(n):
    m = int(sys.stdin.readline())
    lst.append(m)

b = 0; k = 0
for j in range(-1, -(n + 1), -1):
    if lst[j] > b:
        b = lst[j]
        k += 1
print(k)