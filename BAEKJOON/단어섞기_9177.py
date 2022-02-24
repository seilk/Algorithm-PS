# ----------Title
# 단어섞기
# Gold V
# https://boj.kr/9177

# ----------Tip
# BFS + Memoization
# visited가 아닌 excepted
# 색다른 유형이라고 느낀 BFS

# ----------URLs

# ----------Code with Detail
import sys
from collections import deque, defaultdict
def input(): return sys.stdin.readline().rstrip()


def BFS(a, b, c, excepted):
  queue = deque([(0, 0)])
  while queue:
    idx_a, idx_b = queue.pop()

    if idx_a + idx_b == len(c):
      return True

    if idx_a < len(a) and a[idx_a] == c[idx_a + idx_b] and not excepted[idx_a + 1][idx_b]:
      queue.append((idx_a + 1, idx_b))

    if idx_b < len(b) and b[idx_b] == c[idx_a + idx_b] and not excepted[idx_a][idx_b + 1]:
      queue.append((idx_a, idx_b + 1))

    excepted[idx_a][idx_b + 1] = 1
  return False


num = int(input())
sets = [input().split() for i in range(num)]
for i in range(num):
  a, b, c = sets[i]
  excepted = [[0] * (len(b) + 2) for i in range(len(a) + 2)]
  print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " yes")) \
      if BFS(a, b, c, excepted) else\
      print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " no"))
# def check(alpha, beta, gamma):
#   idxPackage = defaultdict(list)
#   length_gamma = len(gamma)
#   length_alpha = len(alpha)
#   for i in range(length_gamma):
#     idxPackage[gamma[i]].append(i)


#   for i in range(0, length_alpha):
#     pre = idxPackage[alpha[0]][i]
#     #앞선 인덱스보다 큰 인덱스여야함
#     save_alpha_idx = [pre]
#     for j in range(len(idxPackage[alpha[i]])):
#       idx = idxPackage[alpha[i]][bisect.bisect_right(idxPackage[alpha[i]], pre)]

#       if idx >= length_gamma or pre > idx:
#         return False
#       save_alpha_idx.append(idx)
#       pre = idx

#       gamma_list = list(gamma)
#       for i in save_alpha_idx:
#         gamma_list[i] = '0'
#       gamma = "".join(gamma_list)
#       gamma = gamma.replace('0',"")
#       if gamma == beta:
#         return True
#     return False

# def DFS(depth, alpha, beta, gamma, alpha_length, gamma_length, visited, idx):
#   gamma_list = list(gamma)
#   alpha_list = list(alpha)
#   if depth == alpha_length:
#     tmp = copy.deepcopy(gamma_list)
#     for i in visited:
#       tmp[i] = "-"
#     if "".join(tmp) == beta:
#       return True
#     return
#   for i in range(idx, gamma_length):
#     if gamma[] != gamma[visited[-1]]:
#       if gamma


# for i in range(sets):
#     alpha, beta, gamma = input().split()
#     if check(alpha, beta, gamma):
#         print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " yes"))
#     else:
#         print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " no"))


# A = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
# n = bisect.bisect_right(A, 1)
# print(A[n])
# def check(alpha, beta, gamma):
  # queue_alpha = deque(list(alpha))
  # queue_beta = deque(list(beta))
  # queue_gamma = deque(list(gamma))
  # idx_alpha = 0
  # idx_beta = 0
  # while queue_gamma:
  #   r = queue_gamma.popleft()
  #   if queue_alpha and queue_beta:
  #     a, b = queue_alpha[0], queue_beta[0]
  #     if r == a == b:
  #       # Flag = True if len(queue_alpha) > len(queue_beta) else False
  #       if Flag:
  #         queue_alpha.popleft()
  #       else :  queue_beta.popleft()
  #       continue
  #   if queue_alpha and r == a:
  #     queue_alpha.popleft()
  #     continue
  #   if queue_beta and r == b:
  #     queue_beta.popleft()
  #     continue
  #   else:
  #     return False
  # return True

# def check(alpha, beta, gamma):
#   idx_alpha = deque([gamma.index(alpha[0])])
#   for i in range(len(alpha)):
#     pre = idx_alpha.popleft()
#     cnt = gamma.count(alpha[i], pre)
#     if pre > cnt:
#       return False
#     :
#       idx_alpha.append(cnt)

#   idx_beta = deque([gamma.index(beta[0])])
#   for i in range(len(beta)):
#     pre = idx_alpha.popleft()
#     cnt = beta.count(alpha[i], pre)
#     if idx_beta > pre:
#       idx_beta.append(cnt)


# def check(alpha, beta, gamma):
#   load = gamma
#   for i in range(len(alpha)):
#     gamma = gamma.replace(alpha[i],"",1)
#   if gamma == beta:
#     pass
#   else :
#     return False
#   #
#   gamma = load
#   for i in range(len(beta)):
#     gamma = gamma.replace(beta[i],"",1)
#   if gamma == alpha:
#     return True
#   else :
#     return False
#   #

# for i in range(sets):
#     alpha, beta, gamma = input().split()
#     if check(alpha, beta, gamma):
#         print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " yes"))
#     else:
#         print("{0}{1}{2}{3}".format("Data set ", i + 1, ":", " no"))


# # 1
# # abc adf abcadf
# str.replace()

# N=int(input())


# def check(word1, word2, word3, idx1, idx2, idx3, result):
#     fail=0
#     if idx3 == len(word3)-1:
#         result=True
#         return result

#     if len(word1) > idx1 and word1[idx1] == word3[idx1+idx2]:
#       a=check(word1, word2, word3, idx1+1, idx2, idx3+1, result)

#     if len(word2) > idx2 and word2[idx2] == word3[idx1+idx2]:
#       a=check(word1, word2, word3, idx1, idx2+1, idx3+1, result)

#     else:
#     return a


# resultList=[]
# for i in range(N):
#     wordList=input().split()
#     print(check(wordList[0], wordList[1], wordList[2], 0, 0, 0, False))
#     result=check(wordList[0], wordList[1], wordList[2], 0, 0, 0)
#     print(result)
#     if(result == 1):
#         resultList.append(True)
#     else:
#         resultList.append(False)
