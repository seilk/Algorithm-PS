import sys
import re
def input(): return sys.stdin.readline().rstrip()
# https://realpython.com/python-lambda/ : lambda Function Detail


kitty = input()
dog = [i for i in kitty if i == "+" or i == "-"]
cat = list(map(int, re.split('[+-]', kitty)))
# 연산자가 +, - 밖에 없고 괄호의 제한이 없으므로 -가 나오는 위치부터 괄호를 이용해서 덧셈을 전부 뺄셈으로 바꿀 수 있다.
# -가 처음 나오는 위치를 저장하고 그 위치부터는 모든 숫자를 전부 뺄셈한다.
if "-" in dog:
    lion = dog.index("-")
else:
    print(sum(cat))
    sys.exit(0)
puma = cat[lion + 1:]
bear = cat[: lion + 1]
for i in range(len(puma)):
    puma[i] *= -1
print(sum(bear) + sum(puma))
