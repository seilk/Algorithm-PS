import sys
sys.setrecursionlimit(10**9)
n = list(sys.stdin.readline().rstrip())  #123 -> ['1', '2', '3']
num = []; #숫자를 만들기 전 저장해두는 리스트
dic = {};  #Permutation을 만드는데 item이 쓰였는지 안쓰였는지 확인하는 dictionary 
maX = -1 #maximum
def f():  #재귀함수
    global maX
    global dic
    global num

    if len(num) == len(n): #num에 추가된 숫자의 길이가 n의 길이(입력된 자리수)와 같으면 maximum 비교한다.
        if int("".join(num)) % 30 == 0: #num에 있는 items는 string이기 때문에 join함수로 묶어서 int로 바꾼 다음 30의 배수를 확인한다.
            maX = max(int("".join(num)), maX) #기존에 저장된 maX보다 크면 갱신한다.
        return

    for i in range(len(n)):  #num에 추가된 숫자의 길이가 n의 길이와 다른경우 for문을 돈다. #재귀함수를 돌때마다 맨 앞부터 i가 시작한다.
        if i in dic: # i가 저장된 x가 dic에 key로 존재하면 loop를 건너뛴다. (전체 loop를 돌면서 숫자를 dic에 있는 숫자와 확인)
            continue 
        if num == [] and n[i] == '0': # num이 빈 리스트고 n[i]가 0이면 loop를 건너뛴다. (0은 가장 앞자리에 올 수 없음)
            continue
        num.append(n[i]); dic[i] = n[i]; # n[i]에 해당하는 수를 num에 append한다. # permutation 확인을 위해서 dic에도 index : value 값으로 저장한다.
        f() # 재귀함수를 돌린다.
        dic.pop(i); num.pop() #dic에서 key가 i인 items를 제거하고 num에서 마지막 자리수를 제거한다.
    return maX

print(f())



