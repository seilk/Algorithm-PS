def solution(n, times):
    # 문제 요구사항 : 모든 인원을 심사하는데 가장 적게 걸리는 시간을 출력
    upper = min(times) * n  # 가장 오래 걸리는 시간 = 가장 짧게 걸리는 데스크의 시간 * 인원 수
    lower = min(times)  # 인원이 1명 이상이기 때문에 최소 걸리는 시간 = 가장 짧게 걸리는 데스크의 시간
    # timeLine = [i for i in range(lower, upper + 1)]
    # 처음에 줄 세울 필요가 없음
    # 이진탐색 : 무조건 숫자들이 갖춰진 list에서 item들을 하나 하나 찍어보며 실행하지 않아도 된다.
    right = upper
    left = lower
    target = n
    while right > left:  # lower bound
        mid = (right + left) // 2
        if target <= howManyPeople(times, mid):
            right = mid
        else:
            left = mid + 1
    return right


def howManyPeople(times, time):  # 해당 시간에 전체 데스크에서 얼마나 많은 인원을 심사할 수 있는지 계산하는 함수
    cnt = 0
    for i in range(len(times)):
        cnt += time // times[i]
    return cnt


print(solution(6, [7, 10]))
