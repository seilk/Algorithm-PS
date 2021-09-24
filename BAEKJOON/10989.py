import sys

n = int(sys.stdin.readline().rstrip())
dic = {}
for i in range(n):
    t = int(sys.stdin.readline().rstrip())
    if t in dic:
        dic[t] += 1
    else:
        dic[t] = 1
sorted_dic = sorted(dic.items(), key=lambda x: x[0])
for i in sorted_dic:
    for j in range(i[1]):
        print(i[0])
