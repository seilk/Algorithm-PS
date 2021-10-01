x = "123"
print(int(x))
y = "a123"
print(int(y))


def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False

    try:
        int(s)
        return True
    except ValueError:
        return False
    return


# s = 'a123'
# def solution(s):
#     if len(s) != 4 and len(s) != 6:
#         return False
#     try:
#         print("aaa")
#         int(s)

#     except Exception as e:
#         print("ERROR", e)
#         return False
#     return True


# solution(s)
