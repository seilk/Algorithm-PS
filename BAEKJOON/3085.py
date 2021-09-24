import sys
n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    lst.append(list(sys.stdin.readline().rstrip()))

def findOnRow(l):
    count_max = 1
    for i in range(len(l)):
        count = 1;
        for j in range(len(l) - 1):
            if l[i][j] == l[i][j + 1]:
                count += 1
            else : count = 1
            count_max = max(count, count_max)
    return count_max

def findOnColumn(l):
    count_max = 1
    for j in range(len(l)):
        count = 1;
        for i in range(len(l) - 1):
            if l[i][j] == l[i + 1][j]:
                count += 1
            else : count = 1
            count_max = max(count, count_max)
    return count_max

answer_lst = set()
for i in range(n):
    for j in range(n - 1):
        if lst[i][j] == lst[i][j + 1]:
            continue
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
        answer = max(findOnRow(lst), findOnColumn(lst))
        if answer == n:
            print(answer)
            sys.exit()
        answer_lst.add(answer)
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

for j in range(n):
    for i in range(n - 1):
        if lst[i][j] == lst[i + 1][j]:
            continue
        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
        answer = max(findOnRow(lst), findOnColumn(lst))
        if answer == n:
            print(answer)
            sys.exit()
        answer_lst.add(answer)
        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]

print(max(answer_lst))