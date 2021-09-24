################################################################################
# 교훈 : A % B 에서 나머지는 절대 A를 넘을 수 없다. 0부터 A - 1까지가 나머지가 된다.#
################################################################################


import sys
def f():
    return map(str, sys.stdin.readline().split())
n, k = f()
n = int(n); k = int(k);
lst = ['?' for i in range(n)]
s = 0
wheel = True

for i in range(k):
    c, x = f() #c is change, x is Alphabet 
    c = int(c)
    
    w = (s + c) % n  # w is new positon, 그냥 오른쪽에 알파벳 넣어주고 마지막에 순서 뒤집으면 됨 (원이라 상관없음) 답에서 첫번째로 읽는 알파벳은 마지막에 넣는 알파벳임
    
    if x in lst: # x가 lst에 존재할 때
        if (w != lst.index(x)) : # Alphabet이 있는 위치와 w가 다를 때
            wheel = False
        else: 
            pass
            

    elif x not in lst: #x 가 lst에 존재하지 않을 때
        if (lst[w] != '?') : #Alphabet이 들어가려는 위치에 다른 Alphabet이 있을 때
            wheel = False
        else:
            lst[w] = x
    
    s = w #시작하는 위치 갱신

if wheel:
    fin = list(reversed(lst[: w + 1])) + list(reversed(lst[w + 1 :])) #
    print(*fin, sep="")
else:
    print("!")
