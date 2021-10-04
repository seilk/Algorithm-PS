import re


def lowerAlpabet(new_id):
    return new_id.lower()  # new_id.lower() << new_id (return)


def cleanString(new_id):
    # clean_id = re.sub('[^0-9a-z-_.]','',new_id) #정규식 쓰는 방법
    clean_id = []
    # ',' 가 없어서 실패했었음.
    unvalid = ['~', '!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', '<', '>', '/', ',']
    for i in range(len(new_id)):
        if new_id[i] not in unvalid:
            clean_id.append(new_id[i])
    return clean_id


def abbDot(clean_id) -> list:
    # while ~ replace("..", ".") 으로도 가능
    new_id = []
    if len(clean_id) == 0 or len(clean_id) == 1:
        new_id = clean_id
    if len(clean_id) > 1:
        new_id.append(clean_id[0])  # [.abcd123.4r] [a] [1]
        for i in range(1, len(clean_id)):
            if clean_id[i] == '.' and clean_id[i] == clean_id[i - 1]:
                continue  # append를 해주지 않는다.
                # .(.) .(..) .(...)
            new_id.append(clean_id[i])
    return new_id


def delSideDot(new_id) -> list:
    if new_id[0] == '.':
        del new_id[0]
    if len(new_id) > 0 and new_id[-1] == '.':
        del new_id[-1]
    return new_id


def emptyId(new_id) -> list:
    if new_id == []:
        new_id = ["a"]
    return new_id


def shortenId(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':  # [12asdasdv]
            del new_id[-1]
    return new_id


def tooShortenId(new_id) -> list:
    while len(new_id) <= 2:
        new_id.append(new_id[-1])
    return new_id


def solution(new_id):
    return "".join(tooShortenId(shortenId(emptyId(delSideDot(abbDot(cleanString(lowerAlpabet(new_id))))))))
