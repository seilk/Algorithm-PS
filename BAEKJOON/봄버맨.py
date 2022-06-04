import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

R, C, N = MIS()

plate = [list(In()) for i in range(R)]

k = 3
for i in range(R) :
	for j in range(C) :
		if plate[i][j] == "O" :
			plate[i][j] = k

def bomb(cur_plate, k) :
	for i in range(R) :
		for j in range(C) :
			if cur_plate[i][j] != k : continue
			for adj_i, adj_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] :
				if adj_i < 0 or adj_j < 0 or adj_i >= R or adj_j >= C : continue
				if cur_plate[adj_i][adj_j] == "." : continue
				if cur_plate[adj_i][adj_j] == k : continue
				cur_plate[adj_i][adj_j] = "."

	for i in range(R) :
		for j in range(C) :
			if cur_plate[i][j] == k:
				cur_plate[i][j] = "."


def bury(cur_plate, k) :
	for i in range(R) :
		for j in range(C) :
			if plate[i][j] == "." :
				plate[i][j] = k+3

for time in range(2, N+1) :

	bury(plate, time)
	if time-3 >= 0 :
		bomb(plate, time)

for i in range(R) :
	for j in range(C) :
		if plate[i][j] != "." :
			plate[i][j] = "O"

for i in range(R) :
	print(*plate[i], sep="")
