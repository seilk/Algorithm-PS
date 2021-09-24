import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
card = []

for _ in range(n):
    card.append(str(sys.stdin.readline().rstrip()))

if k == 1:
    print(n)
else:
    seT = set()  #숫자를 만들기 위한 set
    z = []; num = []
    dic = {}; dic2 = {};  #중복을 피하기 위한 dic
    #key : value
    #index : lst[index]
    # 1 2 2 1 12
    # set / list -> dic
    # 
    def g(): # z = [ '1', '2' ]
        if len(num) == k:  #z에서 k개를 뽑은 순간
            number = int("".join(num))
            seT.add(number)  #set에 num을 추가 
            return
        for __ in range(k):
            if __ in dic2:  #index key가 dic2에 존재하면 다음 loop로 넘어감
                continue
            num.append(z[__]) #z의 원소를 num에 추가 num = [1, 2] [2, 1]
            dic2[__] = z[__]  #중복을 방지하기 위해 dic2에 추가
            g()
            dic2.pop(__); num.pop()

    def f():
        if len(z) == k:  #z에 k개의 카드 들어가 들어가는 순간
            g()
        for _ in range(n): #카드의 장수만큼 loop
            if _ in dic :  #dic에 이미 있는 index면 다음 loop로 넘어감
                continue
            z.append(card[_]) # 1 2 2 1 12
            dic[_] = card[_]  # {0 : 1 , 1 : 2}
            f()
            dic.pop(_); z.pop()

    f()
    print(len(seT))
