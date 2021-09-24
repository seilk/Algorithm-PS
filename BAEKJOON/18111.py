from sys import stdin
import math

h, w, extra_blocks = map(int, stdin.readline().split())  # height , width, blocks
area = h * w
ground = []
for i in range(h):
    ground += list(map(int, stdin.readline().split()))  # 1차원으로 변형

total_blocks = sum(ground) + extra_blocks  # 모든 block의 개수

used_blocks = 0  # 초기 사용 block 개수
height = 0
while True:
    t = 0
    if (max(ground) * area) < (
        used_blocks
    ) or used_blocks > total_blocks:  # 사용된 블록 수는 가장 높이 평평해질 수 있는 경우의 블록수 또는 전체 블록수를 초과하면 의미가 없다.
        break  # 최고 높이 * 면적 보다 사용된 블록 수가 많으면 break (이 조건이 없으면 B가 매우 클 때 계속 의미없는 계산을 함.)
    for j in range(area):  # 면적은 len(ground) 즉 모든 땅을 돌아다니면서 높이를 비교하고 시간을 계산해야함.
        if ground[j] < height:
            t += (height - ground[j]) * 1  # 원래 땅에 쌓은 경우
        else:
            t += (ground[j] - height) * 2  # 원래 땅에서 지운 경우

    if (
        height == 0
    ):  # 맨 처음 높이가 0일 때는 최소시간을 임시저장한 시간으로 할당함(맨 처음이라 temp_t가 min_t라는 논리도 맞음),
        # 초기 최소 시간을 말도 안되게 높게 잡는 AC를 봤는데 논리적으로 타당하지 않아서 차라리 높이가 0일때 예외를 넣어줬다.
        min_t = t
        height_t = height

    elif (
        min_t >= t
    ):  # min 함수를 이용하면 최소 시간을 구하는것은 정말 쉽다. min_t = min(min_t, t) 그러나 최소 시간과 그 시간에서의 높이를 갱신해줘야 하기 때문에 어차피 if (min_t가 바뀌면 어쩌고 저쩌고) 를 써서 height_t를 계산해야 하므로 min_t 와 height_t를 둘다 한 조건문 안에서 할당 할 수 있게 코드를 작성했다.
        min_t = t
        height_t = height
    height += 1  # height는 1씩 증가시킴. 다음 반복문에 들어가는 높이는 1이 증가되어야 한다. 그림을 그리면 쉽게 이해할 수 있다.
    used_blocks = (
        area * height
    )  # 다음번에 사용되는 블록 수 갱신. 다음 반복문에 들어가는 '사용된 블럭은 (면적 * 갱신된 높이)로 갱신되어야 한다.


print(min_t, height_t)
