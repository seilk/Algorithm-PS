import sys
N = int(sys.stdin.readline().rstrip())
group = [0 for i in range(N)] 
for i in range(N):
    group[i] = list(sys.stdin.readline().rstrip())
x = len(group[0])
pattern = [x for x in group[0]]
for i in range(x):
    j = 1
    same = True
    while same and j < N:
        if group[0][i] != group[j][i]:
            same = False
            pattern[i] = "?"
        j += 1

for x in pattern:
    print(x, end='')

