import sys
N = int(sys.stdin.readline().rstrip());
group = list(map(int, sys.stdin.readline().split()));
suM = [x for x in group] # suM = group 하면 group이 변하면 suM이 변한다. group이 가리키는 메모리주소를 suM도 가리키게 됨

suM[0] = group[0]
for i in range(1, N):
    for j in range(i):
        if group[j] < group[i]:
            suM[i] = max(suM[j] + group[i], suM[i])

print(max(suM))
print(suM)

            # 1 -> 1 / 100 / 2 / 50 / 60
            # 100 -> 1 / 101 / 2 / 50 / 60
            # 2 -> 1 / 101 / 3 / 50 / 60
            # 50 -> 1/ 101/ 3/ 51/ 60
            #
