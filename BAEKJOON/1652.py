from sys import stdin
n = int(stdin.readline().rstrip())
room = []
for i in range(n):
    room.append(list(str(stdin.readline().rstrip())))

can = 0
for i in range(n):
    sit = 0
    for j in range(n):
        if room[i][j] == ".":
            sit += 1
            if sit == 2:
                can += 1
        if sit > 2 and room[i][j - 1] == ".":
            pass
        if room[i][j] == "X":
            sit = 0
print(can, end=" ")

can = 0
for i in range(n):
    sit = 0
    for j in range(n):
        if room[j][i] == ".":
            sit += 1
            if sit == 2:
                can += 1
        if sit > 2 and room[j][i - 1] == ".":
            pass
        if room[j][i] == "X":
            sit = 0
print(can)        