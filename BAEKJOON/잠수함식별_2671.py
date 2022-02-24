import re
s = input()
p = re.compile('(100+1+|01)+')
m = re.fullmatch(p, s)
if m:
  print("SUBMARINE")
else:
  print('NOISE')
