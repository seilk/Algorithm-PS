from collections import defaultdict


def DFS(info, dic, score, visited, idx):
    if idx == len(info):
        # key = parsing한 문자열, val = vector(items : score)
        dic["".join(info)].append(score)
        return
    for i in range(2):
        if not visited[i]:  # visited[i] = 0
            pre = info[idx]
            info[idx] = "-"
        # DFS에 idx를 인자로 주면서 info의 다음 item으로 넘어가게 함
        DFS(info, dic, score, [0, 1], idx + 1)
        info[idx] = pre


def solution(infos, queries):
    # info : 언어[0] 직군[1] 경력[2] 소울푸드[3] 점수[4]
    # query : 언어[0] 직군[1] 경력[2] 소울푸드[3] 점수[4]
    ans = []
    dic = defaultdict(list)
    infoArr = []
    for info in infos:  # info 문자열 parsing
        infoArr.append(info.split())

    for info in infoArr:  # parsing한 문자열 배열에서 "-"가 들어갈 수 있는 모든 경우의 수 사전에 추가
        score = int(info.pop())
        DFS(info, dic, score, [0, 1], 0)  # DFS로 구현

    for key in dic:
        if dic[key]:
            dic[key].sort()  # binary search를 위한 오름차순 정렬

    queryArr = []
    for query in queries:  # query parsing
        query = query.replace("and", "")
        queryArr.append(query.split())

    for query in queryArr:
        target = int(query.pop())  # query의 마지막 원소(점수) pop
        key = "".join(query)
        if dic[key]:
            aim = dic[key]  # aim = query와 같은 문자열을 갖는 key의 value(vector)
            left = 0
            right = len(aim)
            while left < right:  # lower bound, right와 left는 한점에서 만나게 된다.
                mid = (left + right) // 2
                if target <= aim[mid]:
                    right = mid
                else:  # aim[mid] < target
                    left = mid + 1  # target보다 작으면 점점 오른쪽으로 밀어서 값을 크게 해야함.
            ans.append(len(aim) - right)
        else:  # query에서 요구하는 조건이 없을수도 있음.
            ans.append(0)
    return ans
    #
    #
    #
    # 효율성을 통과하지 못한 code
    # for query in queryArr:
    #     cnt = 0
    #     for info in infoArr:
    #         i = 0
    #         while i < 5:
    #             if i == 4 and int(query[i]) > int(info[i]):
    #                 break
    #             elif i < 4 and query[i] != "-":
    #                 if info[i] != query[i]:
    #                     break
    #             i += 1
    #         if i == 5:
    #             cnt += 1
    #     ans.append(cnt)
    # return ans


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
    "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
