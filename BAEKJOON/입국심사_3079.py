import sys
def input(): return sys.stdin.readline().rstrip()


desks, people = map(int, input().split())
times = [int(input()) for i in range(desks)]
# 최소 시간을 구하는데
# 가장 짧은 시간 후보들 중에서 가장 긴 시간과 가장 짧은 시간을 구해야한다.
# 가장 빨리 끝나는 데스크의 시간 * 사람수 = 상한
# 가장 빨리 끝나는 데스크의 시간 = 하한 (사람은 최소 1명)
# timeLine = [i for i in range()] ; 이분 탐색에서 items을 반드시 list에 정렬할 필요 없다.
upper = min(times) * people
lower = min(times)
# lower와 upper사이에 최소 시간이 존재한다.
# 해당 시간에 사람을 몇명 심사할 수 있는지 확인하면 됨
# 그리고 target에 맞는 시간중에서 가장 작은 시간을 구하면 정답
# binary search : lower bound
# 해당 시간에 전체 데스크에서 심사할 수 있는 사람을 구하는 방법?
# ex) 5초가 걸리는 데스크에서는 10초동안 2명을 볼 수 있다.
# ex) 17초가 걸리는 데스크에서는 33초 동안 2명을 볼 수 있다.
# 각 데스크 걸리는 시간을 나눠서 몫을 구하면 된다.
#
# lower bound 기본꼴
# while문 사용
# 큰 틀에서 right를 출력하는 방식 사용
left = lower
right = upper
while left < right:  # right와 left가 같아지는 순간 while문 탈출
    mid = (right + left) // 2
    # mid 시간에서 몇명의 인원을 체크할 수 있는지 확인해야함
    cnt = 0
    for time in times:
        cnt += mid // time
    #
    if cnt < people:  # people은 target, target이 오른쪽에 있을 때
        left = mid + 1
    else:  # mid값이 target보다 작거나 같을때 right를 mid에 고정시킴
        right = mid
# left는 조건이 맞으면 mid+1 해주고 right는 조건이 맞으면 mid값으로 고정시키면서 mid값이 target과 일치할 때 right값이 움직이지 않으면서 left값은 +1로 right값에 다가가게 된다.
print(right)
# 번외
# 같은 값이 여러개일경우 최소 구하기
# [1,2,2,2,3,4,5,6]에서 2가 타겟이고 최소 인덱스를 구해야한다고 하자.
# 2가 여러개여서 mid가 2가 되는 순간이 많을것이다.
# 3가지 경우가 있다.
# 1.mid가 target과 일치 -> right가 고정하고 mid는 항상 right보다 왼쪽에 존재하므로 중복으로 mid가 일치하면 다시 right가 mid값으로 왼쪽으로 이동해서 고정되고 일치하지 않는다면 left가 mid + 1로 잡히면서 right와 좁혀진다.
# 2. mid가 target의 오른쪽 -> mid를 왼쪽으로 옮겨서 target을 찾아야함 : right를 mid로 잡고 반복문 시작
# 3. mid가 target의 왼쪽 -> mid를 오른쪽으로 옮겨서 target을 찾아야함 : left를 mid + 1로 잡고 반복분 시작
# 이 때 mid가 아니라 mid + 1인 이유는 mid로 하면 원소가 2개남은 상황에서 mid는 항상 left가 나오기 때문에 반복문이 끝나지 않기 때문이다.
# +1을 해줘도 상관없는 이유는 만약 left가 target이라고 하면 mid값은 right가 되면서 다가갈것이고 mid + 1이 target이라고 하면 계속되는 loop에서 right = mid가 진행되면서 left는 고정된 상태로 right를 기다린다. 기다리다가 mid가 target으로 잡히게 되면 right = mid가 되고 left = right인 상황이 되므로 반복문을 빠져나온다.
#
# upper bound는 left를 고정하고 right를 -1 해주면서 다가가면 된다.
# if mid <= target: left = mid ; else : right = mid - 1 return left
