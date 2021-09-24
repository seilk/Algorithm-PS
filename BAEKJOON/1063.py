import sys
def f():
    return map(str, sys.stdin.readline().split())
N, K = f()
N = int(N); K = int(K);
lst = ['?' for i in range(N)] 
wheel = True
for i in range(K):
    c, x = f() 
    c = int(c)
    w = - (c % N) 
    if i == 0:
        lst[w] = x 

    elif x in lst:
        if ((abs(lst.index(x)) + abs(w)) != N) : 
            wheel = False
            
        else:
            lst[w] = x
            

    elif x not in lst:
        if (lst[w] != '?') :
            wheel = False

        else:
            lst[w] = x

    temp = []
    for i in range(w, N + w, +1): 
        temp.append(lst[i])   
    lst = temp

if wheel:
    for i in range(N):
        print(lst[i], end="")
else:
    print("!")