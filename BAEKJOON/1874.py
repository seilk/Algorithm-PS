import sys
import collections

input = sys.stdin
n = int(input.readline().rstrip())
goal = collections.deque([int(input.readline().rstrip()) for i in range(n)])
goal_copy = list(goal.copy())
ascending = [i for i in range(1, n + 1)]
sol = []
stack = []
log = []
for i in ascending:
<<<<<<< HEAD
  while True:
    if stack and stack[-1] == goal[0]:
      sol.append(stack.pop())
      goal.popleft()
      log.append("-")
    else:
      break
  stack.append(i)
  log.append("+")
=======
    while True:
        if stack and stack[-1] == goal[0]:
            sol.append(stack.pop())
            goal.popleft()
            log.append("-")
        else:
            break
    stack.append(i)
    log.append("+")
>>>>>>> temp2

goal = goal_copy

if stack:
<<<<<<< HEAD
  sol += stack[::-1]
  log += ["-"] * (len(stack))
  if sol != goal:
    print("NO")
  else:
    print(*log, sep="\n")

else:
  print(*log, sep="\n")
=======
    sol += stack[::-1]
    log += ["-"] * (len(stack))
    if sol != goal:
        print("NO")
    else:
        print(*log, sep="\n")

else:
    print(*log, sep="\n")
>>>>>>> temp2
