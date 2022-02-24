from sys import stdin

lst = list(stdin.readline().rstrip())
stack = []
pieces = 0
rod = 0
for i in range(len(lst)):
    if lst[i] == "(":  # (
        stack.append(lst[i])
        if i >= 1 and lst[i - 1] == ")":  # )(
            pieces += rod * 2 + len(stack) - 1
            rod = 0
            continue

    else:  # ")"
        stack.pop()
        if lst[i - 1] == ")":  # 닫힌 괄호가 연속적으로 나올 때
            rod += 1
        if i == len(lst) - 1:
            pieces += rod * 2
        continue

print(pieces)
