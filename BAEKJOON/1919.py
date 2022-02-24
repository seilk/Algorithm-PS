from sys import stdin

p = list(str(stdin.readline().rstrip()))
q = list(str(stdin.readline().rstrip()))

<<<<<<< HEAD
lstp = [0 for i in range(26)]  # alphabet of p
lstq = [0 for i in range(26)]  # alphabet of q
for i in p:
    lstp[ord(i) - 97] += 1  # small a start at 97(dec)
=======
lstp = [0 for i in range(26)] #alphabet of p
lstq = [0 for i in range(26)]  #alphabet of q
for i in p:
    lstp[ord(i) - 97] += 1 # small a start at 97(dec)

>>>>>>> temp2
for i in q:
    lstq[ord(i) - 97] += 1

diff = 0
for i in range(26):
    if lstp[i] == lstq[i]:
        continue
    else:
        diff += abs(lstp[i] - lstq[i])

<<<<<<< HEAD
print(diff)
=======
print(diff) 

>>>>>>> temp2
