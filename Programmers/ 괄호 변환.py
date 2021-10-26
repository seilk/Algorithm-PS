from collections import deque


def check(strng) -> bool:
    stack = []
    for i in list(strng):
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


def solution(strng):
    global ans
    #
    if strng == "" or check(strng):
        return strng
    #
    cnt = [0, 0]
    queue = deque(strng)
    tmpu = []
    while queue:
        i = queue.popleft()
        tmpu.append(i)
        if i == "(":
            cnt[0] += 1
        elif i == ")":
            cnt[1] += 1
    #
        if cnt[0] == cnt[1]:
            break
    #
    u = "".join(tmpu)
    v = "".join(queue)
    if check(u):
        return u + solution(v)
    else:
        x = "(" + solution(v) + ")"
        u = "".join(u[1:len(u) - 1])
        if u != "":
            tmp = list(u)
            for i in range(len(u)):
                tmp[i] = "(" if tmp[i] == ")" else ")"
        return x + "".join(tmp)


# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))
# "()(() )()"
# "()(() ())()"
