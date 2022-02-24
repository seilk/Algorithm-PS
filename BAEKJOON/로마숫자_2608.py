from sys import stdin
input = stdin.readline
# dictionary의 ordering이 중요한 문제
d = {"IV": 4,
     "IX": 9,
     "XL": 40,
     "XC": 90,
     "CD": 400,
     "CM": 900,
     "I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000
     }

dd = {"M": 1000,
      "CM": 900,
      "D": 500,
      "CD": 400,
      "C": 100,
      "XC": 90,
      "L": 50,
      "XL": 40,
      "X": 10,
      "IX": 9,
      "V": 5,
      "IV": 4,
      "I": 1
      }
fst = input().rstrip()
scd = input().rstrip()

ans1 = 0
while fst != "" or scd != "":
  for k, v in d.items():
    if k in fst:
      fst = fst.replace(k, "", 1)
      ans1 += v
    if k in scd:
      scd = scd.replace(k, "", 1)
      ans1 += v

tmp = ans1
ans2 = ""
while tmp > 0:
  for k, v in dd.items():
    if tmp >= v:
      tmp -= v
      ans2 += k
      break

print(ans1)
print(ans2)
