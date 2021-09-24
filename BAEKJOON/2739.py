# import sys
# N = int(sys.stdin.readline().rstrip());
# for i in range(1, 10):
#     print(N,'*',i,'=',N * i)

import sys
TestN = int(sys.stdin.readline().rstrip())
for i in range(TestN):
    StuScores = list(map(int, input().split()))
    StuN = StuScores.pop(0)
    Mean = sum(StuScores) / StuN
    Upper = 0
    for j in range(len(StuScores)):
        if StuScores[j] > Mean:
            Upper += 1
    print("{:.3f}%".format(((Upper/len(StuScores) * 100))))