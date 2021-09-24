import sys
import math
from collections import Counter
word = list(sys.stdin.readline().rstrip())
dic = Counter(word) #word에 들어있는 알파벳별 개수 정리
count = 0

if len(set(word)) == len(word):
    print(math.factorial(len(word)))
    sys.exit()
    
def dfs(depth, pre):
    global count
    if depth == len(word): #재귀함수 종료문
        count += 1
        return
    for key in dic:
        if pre != key:
            if dic[key] == 0:
                continue
            dic[key] -= 1
            dfs(depth + 1, key)
            dic[key] += 1


dfs(0,"nothing")
print(count)