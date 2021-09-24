from sys import stdin

def splitWords(w):
    if w.count("BB") >= w.count("AA"):
        w = "".join(w.split("BB"))
    elif w.count("AA") > w.count("BB"):    
        w = "".join(w.split("AA"))
    return w

n = int(stdin.readline().rstrip())

cnt = 0
for i in range(n):
    w = stdin.readline().rstrip()
    loop = len(w)
    if loop % 2 != 0:
        continue

    for j in range(int(loop)):
        if len(w) % 2 != 0:
            break
        elif len(w) == 0:
            cnt += 1
            break
        w = splitWords(w)        

print(cnt)