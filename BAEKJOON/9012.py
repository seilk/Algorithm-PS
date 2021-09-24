import sys


# 괄호를 계속 소거함.

def f(lst):  #inpuT = [(,(,(,),),),...]
    k = len(lst) # lst의 길이를 range로 for문을 돌림, 매번 갱신됨.
    # ))))만 남아있음 , ((((만 남아있음 , )로 시작, (로 끝남
    if '(' not in lst or ')' not in lst or k == 0 or lst[0] == ")" or lst[-1] == "(": #함수를 더이상 돌릴 필요 없는 조건들 / for문에서 lst는 무언가가 남아있게 됨
        return k #여기서 return 되는 순간 재귀함수 통째로 종료됨, lst는 바뀐상태로 유지 
    else:
        for i in range(k - 1): # i + 1을 쓸거라서 마지막에서 - 1번째 까지만 확인해줘도 됨
            if lst[i] == "(" and lst[i + 1] == ")": # 연속으로 ()가 나오면 소거
                del lst[i : i + 2]
                break  # ()묶음이 한번 지워지면 for문 종료하도록 함      
        return f(lst) # 삭제된 lst를 가지고 함수를 다시 돌림, 재귀함수가 종료되면서 한꺼번에 종료되기 때문에 처음에 return된 값이 계속 return 됨 return(return(return(...)))

for i in range(int(sys.stdin.readline())):
    lst = list(sys.stdin.readline().rstrip())
    if f(lst) != 0: #lst의 괄호를 조건이 맞을 때 까지 소거시키는 함수, 소거가 완료된 lst의 길이를 return함
        print("NO")
    else:
        print("YES")

# lst = [1, 2]
# del lst[0:2]

# print(lst)