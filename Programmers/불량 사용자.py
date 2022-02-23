from collections import defaultdict

def find(banned,user):
  if len(banned) != len(user):
    return False
  for i in range(len(banned)):
    if banned[i]=="*":continue
    elif user[i]!=banned[i]:
      return False
  return True

def backtrk(d, bidx, user_id, banned_id, vistB, vistU, avoidDup, avoidDupDict):
  global ans

  if d == len(banned_id):
    if avoidDupDict[avoidDup]==0:
      avoidDupDict[avoidDup]=1
      ans+=1
    return

    # 순열 : 한명의 불량 사용자당 가능한 아이디를 탐색, 깊이가 불량사용자의 인원수만큼 들어가게 되면 모든 불량 사용자의 아이디 매칭 완료 됐다는 의미
    # 백트래킹으로 다시 빠져 나와서 한명의 불량 사용자에 대한 또 다른 가능한 유저 아이디 추출함.
    # 하나의 콜스택에서는 하나의 불량 사용자만 다뤄야 함. 하나의 콜스택에서 여러명의 불량사용자를 다루면 안됨. n제곱 꼴의 형태가 됨.

  bb=banned_id[bidx]
  for u in range(len(user_id)):
    if not vistU[u] and find(bb, user_id[u]): # 이미 사용된 아이디, 아이디 형식 확인
      vistU[u]=1
      backtrk(d+1, bidx+1, user_id, banned_id, vistB, vistU, avoidDup|(1<<u), avoidDupDict)
      vistU[u]=0

def solution(user_id, banned_id):
  global ans
  ans = 0
  vistU=[0]*len(user_id)
  vistB=[0]*len(banned_id)
  avoidDupDict = defaultdict(int)
  backtrk(0, 0, user_id, banned_id, vistB, vistU, 1<<len(user_id), avoidDupDict)
  return ans

print(solution(["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"],
               ["********","********","********","********","********","********","********","********"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

