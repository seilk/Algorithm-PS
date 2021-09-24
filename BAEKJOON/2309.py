import sys
kids = []
for i in range(9):
    kids.append(int(sys.stdin.readline().rstrip()))
dfs = [0 for _ in range(9)]  #[0, 0, 0, 0, 0, 0, 0, 0, 0]
def isKid(depth):
    if len(height) == 7:
        total = 100
        for j in range(7):
            total -= height[j]
        if total == 0:
            print(*sorted(height), sep="\n")
            sys.exit() #원하는 답이 나오면 프로그램을 exit #올바르게 종료 = 0 #올바르지 않게 종료 = 1 #표시
        return

    for i in range(9):
        if dfs[i]:
            continue
        height.append(kids[i])
        dfs[depth] = 1  #[1, 1, 1, 1, 1, 0, 1, 0, 0]
        isKid(depth + 1)
        height.pop()
        dfs[depth] = 0

height = []
isKid(0)
