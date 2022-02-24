import sys
from collections import defaultdict
from collections import Counter
def input(): return sys.stdin.readline().rstrip()


def solve(lst):
    r_lst = lst[::-1]
    # value와 position을 담은 dict 구현 {1 : (a, b, c, d...), 2 :...}
    target = defaultdict(tuple)
    for i, v in enumerate(lst):
        target[v].append(i)
        target[v].sort()

    for i, v in enumerate(lst):
        target
# 거꾸로 생각해서 뒤에서부터 y가 x의 두배보다 크면 됨.
    for i in range(len(lst)):
        s = r_lst[i + 1:]
        d = Counter(s)


for i in range()
