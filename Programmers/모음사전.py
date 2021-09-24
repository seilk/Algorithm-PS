lst = ['A', 'E', 'I', 'O', 'U']
dic = []
x = []  

def f():

    if len(x) >= 5 :
        x.pop()
        return
    
    else :
        for i in range(5):
            x.append(lst[i])
            if "".join(x) not in dic:
                dic.append("".join(x))
            f()
        if "UUUUU" not in dic:
            x.pop() 
        else:
            return

def solution(word):
    answer = int(dic.index(word)) + 1
    return answer

f()