def solution(numbers):
    answers = []
    for number in numbers:
        x = changeToBits(number)
        for i in range(len(x) - 1, -1, -1):
            if i == len(x) - 1 and x[i] == "0":
                answer = x[:i] + "1" + x[i+1:]
                break
            elif i > 0 and x[i] == "0":
                answer = x[: i] + "10" + x[i + 2:]
                break
            elif i == 0:
                answer = "10" + x[1:]
        answers.append(changeToDec(answer))
    return answers


def changeToBits(n) -> str:
    return bin(n)[2:]


def changeToDec(bits) -> int:
    return int(bits, 2)


# print(solution([7]))
print(solution([21, 7, 10**15]))
