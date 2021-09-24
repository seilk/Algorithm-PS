'''lst = ['a', 'b', 'c', 'd', 1, 2, 3]
lst2 = [x for x in lst]
print(lst2)
'''


import re

def lowerAlpabet(new_id):
    new_id = new_id.lower()
    return new_id

def cleanString(new_id):
    clean_id = re.sub('[^0-9a-z-_.]','',new_id)
    #unvalid = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?','<','>','/']
    # for i in range(len(new_id)):
    #     if new_id[i] not in unvalid:
    #         clean_id.append(new_id[i])
    return list(clean_id)


def abbDot(clean_id):
    new_id = []
    if len(clean_id) == 0:
        return clean_id

    elif len(clean_id) == 1:
        return clean_id

    elif len(clean_id) > 1:
        new_id.append(clean_id[0])
        for i in range(1, len(clean_id)):
            if clean_id[i] == '.':
                if clean_id[i] == clean_id[i - 1]:
                    continue
                else:
                    new_id.append(clean_id[i])
            else :
                new_id.append(clean_id[i])
        return new_id


def frontDotendDot(new_id):
    if len(new_id) > 0:
        if new_id[0] == '.' :
            del new_id[0]
        if len(new_id) > 0 and new_id[-1] == '.' :
            del new_id[-1]
        return new_id

    else :
        return new_id


def insert_a(new_id):
    if new_id == "" or new_id == []:
        new_id = ["a"]
        return new_id
    return new_id


def shortenId(new_id):
    if len(new_id) >= 16:
        del new_id[15:]
        if new_id[14] == '.':
            del new_id[14]
        return new_id
    return new_id

def tooShortenId(new_id):
    while len(new_id) <= 2:
        new_id.append(new_id[-1])
    return new_id

def solution(new_id):
    answer_lst = tooShortenId(shortenId(insert_a(frontDotendDot(abbDot(cleanString(lowerAlpabet(new_id)))))))
    answer = answer_lst[0]
    for i in range(1, len(answer_lst)):
            answer += answer_lst[i]
    return answer

# .2.
print(solution("~!@#$%&*()=+[}{]:?,<>/"))



