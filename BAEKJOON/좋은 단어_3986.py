import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
def findGoodWord(w : list) -> bool:
    dq = deque(w)
    stack = []
    while dq:
        s = dq.popleft()
        if not stack:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
        else: stack.append(s)
    if stack: return False
    return True


if __name__=="__main__":
    N = int(In())
    ans = 0
    for i in range(N):
        if findGoodWord(list(In())):
            ans+=1
    print(ans)