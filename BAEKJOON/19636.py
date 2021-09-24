import sys
import math

W0, I0, T = map(
    int, sys.stdin.readline().split()
)  # 처음체중, 다이어트 전 일 섭취량(다이어트 전 일 기초 대사량), 역치
D, I, A = map(
    int, sys.stdin.readline().split()
)  # 다이어트 기간, 다이어트 중 일 섭취량, 다이어트 중 일 활동 대사량

W = W0
x = True
for _ in range(D):  # 기초대사량 변화 고려 X
    R = I0 + A
    W += I - R
    if W <= 0:
        x = False
        break
if not x:
    print("Danger Diet")
else:
    print(W, I0)

W = W0  # 몸무게 initialization
K = I0  # 기초대사량 initialization
x = True  # danger initialization
for _ in range(D):  # 기초대사량 변화 고려 O
    R = K + A  # 일 에너지 소비량 = 일 기초 대사량(다이어트 첫째날은 기초대사량 동일) + 일 활동 대사량
    W += I - R  # 체중 = 체중 + (일 에너지 섭취량 - 일 에너지 소비량)
    if abs(I - R) > T:
        K += math.floor((I - R) / 2)  # 기초대사량 (변화) = 기초대사량 + (일 에너지 섭취량 - 일 에너지 소비량)/2
    if W <= 0 or K <= 0:
        x = False
        break
if not x:
    print("Danger Diet")
else:
    print(W, K, end=" ")
    print("YOYO") if (I0 - K) > 0 else print("NO")
