from itertools import permutations
cnt = 0

# dfs
# depth == 3 return
# "17" : 7 17 71 --> 3
# "__" depth == 2 return
# 7! = 5040
# 연산의 수 <= 1억 : 무조건 완탐 가능!
# "17" -> (1) (7) (17) (71)


def solution(numbers):
    global cnt
    lst = list(numbers)
    for i in range(1, len(numbers) + 1):
        per = set(permutations(lst, i))  # permutation(<<iterable>>, m)
        # 011 i = 2 -> {(0, 1), (1, 0)}
        for i in per:
            if i[0] == "0":
                continue
            if isPrime(int("".join(i))):
                cnt += 1
    return cnt


def isPrime(n) -> bool:
    if n <= 1:
        return False

    for i in range(2, n + 1):  # i / 2
        if i * i > n:
            break
        elif n % i == 0:
            return False
    return True
