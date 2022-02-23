from itertools import permutations
from collections import defaultdict

def find(banned, user):
  if len(banned)!=len(user):
    return False
  for i in range(len(banned)):
    if banned[i]=="*":continue
    elif user[i]!=banned[i]:
      return False
  return True


def solution(user_id, banned_id):
  bl = len(banned_id)
  ul = len(user_id)
  dix = dict()
  for i in range(len(user_id)):
    dix[user_id[i]]=i
  userPermutation = permutations(user_id, bl)
  ans=0
  avoidDupDict = defaultdict(int)
  for permu in userPermutation:
    vist = [0]*bl
    g=True
    for per in permu:
      f=False
      for i in range(bl):
        if not vist[i] and find(banned_id[i], per):
          f=True
          vist[i]=1
          break
      if f == False:
        g=False
        break
    if g:
      mask = 1<<ul
      for i in range(bl):
        mask|=1<<dix[permu[i]]
      if avoidDupDict[mask] == 0:
        avoidDupDict[mask] = 1
        ans+=1
  return ans

# print(solution(["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"],
#                ["********","********","********","********","********","********","********","********"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))