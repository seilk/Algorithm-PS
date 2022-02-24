# ----------Title
# 단어 암기
# Gold IV
# https://boj.kr/18119

# ----------Tip
# BitMask
# 단어마다 알고 있는 단어를 비트마스킹 처리해서 저장 하고 쿼리 한번 마다 비트마스킹을 돌면서 & 비교 해주면 되는 문제

# ----------URLs


# ----------Code with Detail
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
words = []  # 단어별 bit가 저장됨
tot = 1 << 26  # initialization : 쿼리에 따라 변하는 비트

dt = dict()  # 알파벳별 shift
opt = dict()  # 최적화를 위한 {알파벳 : 알파벳을 가지는 word}
for i in range(97, 123):
  dt[chr(i)] = 1 << (i - 97)  # dt['a'] = 1 dt['b'] = 2

for i in range(n):  # 단어의 개수
  wb = 1 << 26  # initialization : 단어
  word = set(list(input().rstrip()))  # 단어별 포함된 알파벳 분류
  for apb in word:  # word의 알파벳별 loop
    wb |= dt[apb]
    tot |= dt[apb]

  for apb in word:  # 최적화 dict에 알파벳 : 알파벳을 가지는 word 저장
    try:
      opt[apb].append(wb)
    except:
      opt[apb] = [wb]

  words.append(wb)


# query
ans = n
lst = []
for query in range(m):
  c, apb = map(str, input().split())
  if c == "1":  # forget(XOR)
    try:  # keyError 방지
      for wb in opt[apb]:  # 쿼리에 입력된 문자에 대해서만 loop
        if tot & wb == wb:  # forget 상황이므로 --
          ans -= 1
      tot ^= dt[apb]
    except:
      pass

  elif c == "2":  # memory(OR)
    tot |= dt[apb]  # 단어 암기
    try:  # keyError 방지
      for wb in opt[apb]:
        if tot & wb == wb:  # memory 상황에서는 단어를 추가로 암기했는지를 판단
          ans += 1
    except:
      pass
  print(ans)


# ----------CounterExample(1)
# 3 1
# a
# a
# a
# 1 b
# : keyerror (try/except 없었을때)

# ----------CounterExample(2)
# 3 1
# a
# a
# a
# 1 a
# : 출력초과 (opt를 set으로 했을때 ; 같은 단어가 여러개 나오는 경우가 있으므로 set이 아니라 list로 처리 해줘야함)
