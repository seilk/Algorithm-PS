import sys
import math
day, night, V = (map(int, sys.stdin.readline().split()))
if (V - day) % (day - night) == 0:
    print(int((V - day) / (day - night) + 1))
else:
    print(int(math.ceil((V - day) / (day - night)) + 1))