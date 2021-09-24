def d(n, seT):
    if n > 10000:
        return 
    lst = list(str(n))
    for i in range(len(lst)):
        n += int(lst[i])
    seT.add(n)
    d(n, seT)
    return seT
nonSelfNumber = set()

for i in range(1, 10001):
    if i not in d(i, nonSelfNumber):
        print(i)

