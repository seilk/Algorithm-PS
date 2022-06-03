import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N, M = MIS()
board = [list(In()) for i in range(N)]

def tilt(cmd, red_pos, blue_pos) :
	red_x, red_y = red_pos
	blue_x, blue_y = blue_pos
	if cmd == "right" :
		red_y += 1
		while board[red_x][red_y] == "." :
			red_y += 1
		blue_y += 1
		while board[blue_x][blue_y] == "." :
			blue_y += 1

	if cmd == "left" :
		red_y -= 1
		while board[red_x][red_y] == "." :
			red_y -= 1
		blue_y -= 1
		while board[blue_x][blue_y] == "." :
			blue_y -= 1

	if cmd == "up" :
		red_x -= 1
		while board[red_x][red_y] == "." :
			red_x -= 1
		blue_x -= 1
		while board[blue_x][blue_y] == "." :
			blue_x -= 1

	if cmd == "down" :
		red_x += 1
		while board[red_x][red_y] == "." :
			red_x += 1
		blue_x += 1
		while board[blue_x][blue_y] == "." :
			blue_x += 1

	return (red_x, red_y), (blue_x, blue_y)

red_pos = None
blue_pos = None
for i in range(N) :
	for j in range(M) :
		if board[i][j] == "R" :
			red_pos = (i, j)
			board[i][j] = "."
		if board[i][j] == "B" :
			blue_pos = (i, j)
			board[i][j] = "."

count = 0
dq = deque([[red_pos, blue_pos, count, None]])
flg = False
ans = 11

def get_distance(p_x, new_p_x, p_y, new_p_y) :
	return abs(p_x-new_p_x)+abs(p_y-new_p_y)

while dq :
	red_pos, blue_pos, count, pre = dq.popleft()
	red_x, red_y = red_pos
	blue_x, blue_y = blue_pos
	if count > 10 : continue
	for cmd in ["right", "left", "up", "down"] :
		if pre == "left" and cmd == "right": continue
		if pre == "right" and cmd == "left" : continue
		if pre == "up" and cmd == "down" : continue
		if pre == "down" and cmd == "up" : continue
		new_red_pos, new_blue_pos = tilt(cmd, red_pos, blue_pos)
		new_red_x, new_red_y = new_red_pos
		new_blue_x, new_blue_y = new_blue_pos

		if board[new_blue_x][new_blue_y] == "O" :
			continue
		elif board[new_red_x][new_red_y] == "O" :
			flg = True
			break
		elif new_blue_pos == new_red_pos :
			blue_dist = get_distance(blue_x, new_blue_x, blue_y, new_blue_y)
			red_dist = get_distance(red_x, new_red_x, red_y, new_red_y)
			if blue_dist < red_dist :
				if cmd == "right" :
					new_blue_pos_edit = (new_blue_x, new_blue_y-1)
					new_red_pos_edit = (new_red_x, new_blue_y-2)
				if cmd == "left" :
					new_blue_pos_edit = (new_blue_x, new_blue_y+1)
					new_red_pos_edit = (new_red_x, new_blue_y+2)
				if cmd == "up" :
					new_blue_pos_edit = (new_blue_x+1, new_blue_y)
					new_red_pos_edit = (new_blue_x+2, new_red_y)
				if cmd == "down" :
					new_blue_pos_edit = (new_blue_x-1, new_blue_y)
					new_red_pos_edit = (new_blue_x-2, new_red_y)

			else :
				if cmd == "right" :
					new_blue_pos_edit = (new_blue_x, new_red_y-2)
					new_red_pos_edit = (new_red_x, new_red_y-1)
				if cmd == "left" :
					new_blue_pos_edit = (new_blue_x, new_red_y+2)
					new_red_pos_edit = (new_red_x, new_red_y+1)
				if cmd == "up" :
					new_blue_pos_edit = (new_red_x+2, new_blue_y)
					new_red_pos_edit = (new_red_x+1, new_red_y)
				if cmd == "down" :
					new_blue_pos_edit = (new_red_x-2, new_blue_y)
					new_red_pos_edit = (new_red_x-1, new_red_y)
		else :
			if cmd == "right" :
				new_blue_pos_edit = (new_blue_x, new_blue_y-1)
				new_red_pos_edit = (new_red_x, new_red_y-1)
			if cmd == "left" :
				new_blue_pos_edit = (new_blue_x, new_blue_y+1)
				new_red_pos_edit = (new_red_x, new_red_y+1)
			if cmd == "up" :
				new_blue_pos_edit = (new_blue_x+1, new_blue_y)
				new_red_pos_edit = (new_red_x+1, new_red_y)
			if cmd == "down" :
				new_blue_pos_edit = (new_blue_x-1, new_blue_y)
				new_red_pos_edit = (new_red_x-1, new_red_y)
		if new_red_pos_edit == red_pos and new_blue_pos_edit == blue_pos:
			continue
		dq.append([new_red_pos_edit, new_blue_pos_edit, count+1, cmd])

	if flg :
		ans = min(ans, count + 1)
		break

print(-1 if ans > 10 else ans)