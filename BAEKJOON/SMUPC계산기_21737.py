import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


opr = int(input())  # 수식에 들어갈 기호의 개수.
numSet = [str(i) for i in range(10)]
nums = deque([])
oprs = deque([])
stack = []
stackC = []
count_C = 0
queue = deque(list(input()))

for i in (queue):
    if i in numSet:
        stack.append(i)
    else:
        oprs.append(i)
        if stack:
            nums.append(int("".join(stack)))
        stack = []

save = nums.popleft()
while nums or oprs:
    if oprs:
        y = oprs.popleft()
        if y == "C":
            count_C += 1
            stackC.append(save)
            continue

    if nums:
        x = nums.popleft()
    else:
        break

    if y == "S":
        save -= x
    if y == "M":
        save *= x
        if y == "U":
            save = int(save / x)
    if y == "P":
        save += x

if count_C == 0:
    print("NO OUTPUT")
else:
    print(*stackC, sep=" ")
lst = ["0", "1", "2"]
print(int("".join(lst)))


# print(-5 // 2)  # -2.xx = -3 + postive
# print(int(-5 / 2))  # -2
# print(5 // 2)
