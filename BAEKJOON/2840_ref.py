import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
lst = ['?' for _ in range(n)]
cur = 0
dic = {} #key = Alphabet, value = Index

for _ in range(k):
    m, s = map(str, input().split())
    cur = (cur+int(m)) % n
    if lst[cur] == '?': #cur 위치가 알파벳이 아닌 경우
        if s in dic.keys(): #dic에 s라는 알파벳이 key로 존재할 때 -> lst에 Alphabet이 이미 존재할 때
            print('!')
            sys.exit()
        lst[cur] = s
        dic[s] = cur #dic에 s : cur 형태로 알파벳과 위치를 저장
    elif lst[cur] == s:
        pass #cur위치에 Alphabet이 있지만 그게 s와 같은 경우는 그냥 pass
    else: #cur 위치가 Alphabet이 있는 경우 그러나 s가 아닌 다른 알파벳인 경우
        print('!')
        sys.exit()

lst = list(reversed(lst[:cur+1])) + list(reversed(lst[cur+1:]))
print(*lst, sep='')