
def solution(strng) -> int:
    # 압축은 len(strng) / 2까지 도는게 최대임
    # 주기가 없을때는 그냥 원본의 길이를 출력

    itr = int(len(strng) / 2)
    minleng = len(strng)
    for i in range(1, itr + 1):
        cnt = 1
        ans = ""
        x = ""
        for j in range(0, len(strng), i):
            q = strng[j: j + i]
            if q == strng[j + i: j + 2 * i]:
                cnt += 1

            else:
                ans += str(cnt) + q if (cnt > 1) else q
                cnt = 1
        minleng = min(len(ans), minleng)
    return minleng


print(solution("aabbaccc"))
print(solution("abcabcabcabcdededededede"))
