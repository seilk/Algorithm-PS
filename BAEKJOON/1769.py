n = input()
for i in range(5):
    if len(n) == 1:
        print(i)
        print("NO" if int(n) % 3 else "YES")
        break
    t = 0
    for i in n:
        t += int(i)
    n = str(t)
