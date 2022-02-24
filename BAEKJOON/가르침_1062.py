from collections import defaultdict
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()


mustLearn = {'a', 'n', 't', 'i', 'c'}
n, k = map(int, input().split())
words = [set(list(input()[4:-4])) for i in range(n)]
#
for i in range(n):
    words[i] -= mustLearn
#
wordToBits = [] 
proposed = set()
for word in words:
    tmp = 1 << 26 #10000...000
    for w in word:
        tmp |= 1 << ord(w) - ord('a')
        proposed.add(ord(w) - ord('a'))
    wordToBits.append(tmp)
#
alphabet = 1 << 26 
alphabet |= 1 << ord('a') - ord('a')
alphabet |= 1 << ord('n') - ord('a')
alphabet |= 1 << ord('t') - ord('a')
alphabet |= 1 << ord('i') - ord('a')
alphabet |= 1 << ord('c') - ord('a')
#
ans = 0
pre = alphabet 
if k - 5 >= 0:
    sel = len(proposed) if k - 5 >= len(proposed) else k - 5
    combies = combinations(proposed, sel)
    for combi in combies:
        cnt = 0
        for learn in combi:
            alphabet |= 1 << learn
        for target in wordToBits:
            if alphabet & target == target: 
                cnt += 1
        ans = max(ans, cnt)
        alphabet = pre
    print(ans)
else:
    print(0)


# def DFS(remain, alphabet, selected):
#     global ans
#     if remain <= 0:
#         selected.sort()
#         key = "".join(selected)
#         if not check[key]:
#             check[key] += 1
#             cnt = 0
#             for word in wordToBits:
#                 if alphabet & word != word:
#                     continue
#                 else:
#                     cnt += 1
#             ans = max(ans, cnt)
#         return
#     for i in proposed:
#         if not alphabet & 1 << i:
#             alphabet |= 1 << i
#             DFS(remain - 1, alphabet, selected + [chr(i + 97)])
#             alphabet ^= 1 << i


# #
# if k - 5 >= 0:
#     DFS(k - 5, alphabet, [])
#     print(ans)
# else:
#     print(0)
# def DFS(remain, words, cnt, learning, book, valid):
#     global ans
#     if remain == 0:
#         learning.sort()
#         char = "".join(learning)
#         if not check[char]:
#             check[char] += 1
#             mod = set()
#             for key, val in book.items():
#                 if val:
#                     mod |= set(val)
#             ans = max(ans, n - len(mod))
#             return
#     for i in valid:
#         if not alphabet[i]:
#             pre = copy.deepcopy(book[i])
#             alphabet[i] = 1
#             book[i] = []
#             DFS(remain - 1, words, cnt, learning+[chr(i + 97)], book, valid)
#             book[i] = copy.deepcopy(pre)
#             alphabet[i] = 0


# DFS(k - 5, words, 0, [], book, valid)
# print(ans)

# entries = [word for word in words if len(word) == len(words[0])]
# check = [0] * len(entries)
# for i, entry in enumerate(entries):
#     for word in words:
#         if entry & word == entry:
#             check[i] += 1
# fix = words[check.index(max(check))]
# while remain >= 0:
#     tmp = deque([])
#     while words:
#         word = words.popleft() - fix
#         if word:
#             tmp.append(word)
#     words = copy.deepcopy(tmp)
#     if words:
#         remain -= len(words[0])
#         if remain < 0:
#             break
#     else:
#         break
#     entries = [word for word in words if len(word) == len(words[0])]
#     check = [0] * len(entries)
#     for i, entry in enumerate(entries):
#         for word in words:
#             if entry & word == entry:
#                 check[i] += 1
#     fix = words[check.index(max(check))]

# print(n - len(words))
# if k - 5 < 0:
#     print(0)
# else :

# import sys
# from itertools import combinations
# input = sys.stdin.readline


# def change(temp):
#     res = []
#     for i in temp:
#         res.append(ord(i)-ord('a'))
#     return res
#########
# ans = 0
# poss = 0
# n, k = map(int, input().split())
# if k >= 5:
#     num = set()
#     data = []
#     for i in range(n):
#         t = change(set(input().rstrip()[4:-4])-set(['a', 'n', 'i', 't', 'c']))
#         if len(t) == 0:
#             poss += 1
#             continue
#         num |= set(t)
#         data.append(t)
#     for i, r in enumerate(data):
#         q = 0
#         for a in r:
#             q |= (1 << a)
#         data[i] = q
#     temp = 0
#     temp |= 1 << (ord('a')-ord('a'))
#     temp |= 1 << (ord('n')-ord('a'))
#     temp |= 1 << (ord('t')-ord('a'))
#     temp |= 1 << (ord('i')-ord('a'))
#     temp |= 1 << (ord('c')-ord('a'))
#     if len(num) < k-5:
#         print(n)
#     else:
#         for i in combinations(num, k-5):
#             t = temp
#             cnt = 0
#             for j in i:
#                 if not t & (1 << j):
#                     t |= 1 << j
#             t ^= (1 << 26)-1
#             for d in data:
#                 if d & t == 0:
#                     cnt += 1
#             ans = max(ans, cnt)
#         print(ans+poss)
# else:
#     print(0)
