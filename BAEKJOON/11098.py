import sys

for i in range(int(sys.stdin.readline().rstrip())):
    dic = {}
    for j in range(int(sys.stdin.readline().rstrip())):
        p, q = map(str, sys.stdin.readline().split())
        dic[int(p)] = q
    print(dic[max(dic.keys())])
