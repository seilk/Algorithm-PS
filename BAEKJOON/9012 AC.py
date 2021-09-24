# bracket은 항상 짝이 맞아야함
# 따로 뽑아가면서 개수를 체크해줌 (개수가 맞는지, 처음에 '('가 시작되는지, )
# 뭔가 답이 안나올때는 다른 공간을 생각하라

T = int(input())
for t in range(T):
    brackets = input()
    st = []
    flag = False
    for bracket in brackets:
        if bracket == "(":
            st.append(bracket)
        elif bracket == ")":
            if len(st) == 0: # "("가 없는 상태에서 ")" 가 찍힐 때
                flag = True
                print('NO')
                break
            else:
                st.pop()
    if not flag:
        if len(st) > 0:
            print('NO')
        else:
            print('YES')