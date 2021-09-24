import sys
def f():
    return sys.stdin.readline().rstrip()
h, w = map(int, f().split())
time = [[0 for i in range(w)] for i in range(h)]
joi = []
for i in range(h):
    joi.append(list(f()))
    for j in range(w - 1, -1, -1):
        if joi[i][j] == 'c':
            time[i][j] == 0
            continue
        elif j >= 0 :
            for k in range(j, -1 , -1):
                if joi[i][k] == 'c':
                    time[i][j] = j - k
                    break
                else:
                    time[i][j] = -1

    print(' '.join(map(str, time[i])))
