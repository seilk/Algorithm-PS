# # 정해진 길이로 문자열 압축하기
# # 가장 긴 반복 문자 찾기

# #["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# # 1234 muzi로 enter
# # 4567 prodo로 enter
# # 1234 muzi로 leave
# # 1234 prodo로 enter
# # 4567 ryan으로 이름변경

# #["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# # 나간다음 변경, 채팅방에서 변경
# # 채팅방에 있던 메세지도 전부 변경
# # 닉네임 중복허용
# # 데이터 10만개
# # 순차적으로 변경하나?
# # 아이디로 정렬하나?
# # change, 마지막으로 들어온 상황에서의 nickname
# # 이미 나온 id이면
# # [0]이 enter이면 leave이면 change이면에 따라서 달라질듯.
# # 로그를 작성하면서 최종제출을 하는가
# # 최종로그를 한번에 출력하는가
# # ~님이 들어왔습니다.
# # 유저 아이디별로 로그를 작성?
# # 10만개 dict 감당가능한가?
# # user id 별로하면 시간벼롤 log를 잡기가 힘들것 같음
# # 로그를 쓰면서 바꾸는게 최선인듯
import re
from collections import defaultdict
book = defaultdict(str)


def solution(log) -> list:
    ans = []
    for i in range(len(log)):
        tmp = list(map(str, log[i].rstrip().split()))
        if tmp[0] == "Enter":
            book[tmp[1]] = tmp[2]
            ans.append(tmp[1] + "님이 들어왔습니다.")

        elif tmp[0] == "Leave":
            ans.append(tmp[1] + "님이 나갔습니다.")
        elif tmp[0] == "Change":
            book[tmp[1]] = tmp[2]

    # ans에서 id부분을 찾아야함.

    for i in range(len(ans)):
        idx = ans[i].find("님")
        rep = ans[i][:idx]
        ans[i] = ans[i].replace(rep, book[rep])

    for i in range(len(ans)):
        rep = "".join(re.compile('[a-zA-Z0-9]').findall(ans[i]))
        ans[i] = ans[i].replace(rep, book[rep])

    return ans


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
         "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
# import re
# from collections import defaultdict
# example1 = defaultdict(str)
# example2 = dict()

# for i in range(10):
#     example1[i] += "a"
# print(example1)
