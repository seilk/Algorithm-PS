################################################################################
# 교훈 : A % B 에서 나머지는 절대 A를 넘을 수 없다. 0부터 A - 1까지가 나머지가 된다.#
################################################################################

import sys
def f():
    return map(str, sys.stdin.readline().split())
N, K = f() # 5, 6
N = int(N); K = int(K);
lst = ['?' for i in range(N)] 
s = 0
wheel = True
for i in range(K):
    c, x = f() 
    c = int(c)
    w = - (c % N) # 시작값에서 왼쪽으로 이동.. 한바퀴 넘어가는 경우 때문에 나머지 계산

    if x in lst: # x가 lst에 존재할 때
        if ((abs(lst.index(x)) + abs(w)) != N and lst.index(x) + w != 0) : #나머지(w)는 -N이 나올 수 없음
            wheel = False
            # print('i')
        else:
            lst[w] = x

    elif x not in lst:
        if (lst[w] != '?') :
            wheel = False
            # print('j')
        else:
            lst[w] = x
            
    temp = []
    for i in range(w, N + w, 1): #항상 시작하는 값이 인덱스 0 이도록 설정
        temp.append(lst[i])   
    lst = temp
    # print(lst)

if wheel:
    for i in range(N):
        print(lst[i], end="")
else:
    print("!")