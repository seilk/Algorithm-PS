import sys

input = sys.stdin
s = input.readline().rstrip()  # 최대 50자리


def adder(string):  # one adder
    lst = list(string)
    l = len(string)
    for i in range(l - 1, -1, -1):
        if lst[i] == "0":
            if i == 0:
                return -1
            elif i == l - 2:
                lst[i] = "1"
                break
            else:
                lst[i] = "1"
                lst[i + 1] = "0"
                break
    new_string = "".join(lst)
    return new_string


print(adder(s))
