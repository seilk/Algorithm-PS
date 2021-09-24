import sys
def f(): #여러개의 숫자를 입력하면 int 요소의 list return. 숫자 하나를 입력하면 int 하나를 출력하는 함수
    n = sys.stdin.readline()
    if ' ' not in n:
        return int(n)
    else:
        lst = list(map(int, n.split()))
        return lst

def c(lst, indeX): #switch change func return list whice changed number
    if lst[indeX]:
        lst[indeX] = 0
    else:
        lst[indeX] = 1
    return lst
##############################################################
nos = f()  #number of switch
p = f(); p.insert(0, 9)  #switch set #n번째 스위치의 index = n
s = f() #student number
for i in range(s): # 학생 수 만큼 loop
    student = f()  #학생의 정보 (list)
    if student[0] - 1:  #여학생 = 2번, 2 - 1 = true
        c(p, student[1]) #여학생 번호는 무조건 change
        lst1 = list(reversed(p[: student[1]])) #스위치 현황에서 처음부터 여학생 번호 전까지 리스트 따고 뒤집음
        lst2 = list(p[student[1] + 1 :]) #스위치 현황에서 여학생 번호 앞부터 리스트 따고 뒤집음
        for k in range(min(len(lst1), len(lst2))): #두 리스트중에서 길이가 작은걸로 for문 돌림
            if lst1[k] == lst2[k]:  #리스트의 값이 동일한경우
                c(p, student[1] + (k + 1));  c(p, student[1] - (k + 1))
            else:
                break

    else:  #남학생 = 1번
        for j in range(1, nos + 1): #1번부터 nos번까지 loop
            if j % student[1] == 0: #남학생 정보와 배수인 스위치
                c(p, j)  #스위치 변경

pp = list(p[1:])
if len(pp) > 20:
    j = len(pp) // 20
    for j in range(1, j + 1):
        tmp = pp[20 * (j - 1) : 20 * j]
        print(*tmp, sep = " ")#[0 1 ... 19] [20 21 ... 39] [40 41 ... 59]
    tmp = pp[20 * j :] #[나머지]
    print(*tmp, sep = " ")
else : print(*pp, sep=" ")
