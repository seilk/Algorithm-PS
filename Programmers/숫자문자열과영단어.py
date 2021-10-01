def solution(s):
    numbers = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in numbers:
        s = s.replace(i, numbers[i])
    return int(s)


print(solution("two4fivezero"))
