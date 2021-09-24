import sys
from operator import itemgetter
n = int(sys.stdin.readline().rstrip())
book = [[0 for i in range(3)] for i in range(n)]
for _ in range(n):
    tmp = list(map(str, sys.stdin.readline().split())) 
    tmp.insert(2, _) 
    tmp[0] = int(tmp[0])
    book[_] = tmp
book.sort(key=itemgetter(0, 2)) #lambda
for _ in range(n):
    print(*book[_][0:2], sep=" ")

# [[나이, 이름, 인덱스], [나이, 이름, 인덱스], [나이, 이름, 인덱스], [나이, 이름, 인덱스]]