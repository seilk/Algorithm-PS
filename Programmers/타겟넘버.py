# n개의 음이 아닌 정수
# 더하기 혹은 빼기
# 숫자의 개수는 2~20개
# 숫자는 고정시키고 덧셈 뺼셈만 조정해주면 됨
# 시간복잡도 : 2^20
ansSet = set()
x = []


def solution(numbers, target) -> int:
    minus = [1, -1]

    def DFS(idx, cnt):
        if idx == len(numbers):
            if sum(numbers) == target:
                cnt += 1
            return cnt
        for i in range(2):
            numbers[idx] *= minus[i]
            cnt = DFS(idx + 1, cnt)
            numbers[idx] *= minus[i]
        return cnt
    return DFS(0, 0)


print(solution([1, 1, 1, 1, 1], 3))
#
