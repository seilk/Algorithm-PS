from collections import deque


def solution(s):
    ans = ""
    x = deque(s.split())
    while x:
        word = x.popleft()
        for i in range(len(word)):
            c = word[i: i + 1].upper() if i & 1 != 1 else word[i: i + 1].lower()
            word = word[: i] + c + word[i + 1:]
        ans += word + " "
    return ans[:-1]


print(solution("try hello world"))
print(solution(" ABCD abcd AbCd "))
# http://ml-ko.kr/whirlwindtourpython/14-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC%20%EC%A0%95%EA%B7%9C%20%ED%91%9C%ED%98%84%EC%8B%9D.html

# https://skgudwn34.tistory.com/10
