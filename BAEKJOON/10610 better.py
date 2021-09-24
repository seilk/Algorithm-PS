import sys
n = list(sys.stdin.readline().rstrip())  #123 -> ['1', '2', '3']
g = int("".join(reversed(sorted(n)))) # 한방에 내림차순으로 list만들어주는 함수 찾아보기
maX = -1
i = 0
for j in list(str(g)):
    i += int(j)
if '0' not in n or i % 3 != 0: pass #n에 0이 없거나 0을 제외한 모든 수의 합이 3의 배수가 아니면 pass
else: maX = g #0도 있고 수의 합이 3의 배수여야함
print(maX)

