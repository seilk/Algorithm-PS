import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def moving(cmd) :
	com = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동, 서, 북, 남
	return com[cmd]

def roll(pre, cmd) :
	nxt = [[pre[0], pre[4], pre[2], pre[1], pre[6], pre[5], pre[3]],  # 동
	       [pre[0], pre[3], pre[2], pre[6], pre[1], pre[5], pre[4]],  # 서
	       [pre[0], pre[5], pre[1], pre[3], pre[4], pre[6], pre[2]],  # 북
	       [pre[0], pre[2], pre[6], pre[3], pre[4], pre[1], pre[5]]]  # 남
	return nxt[cmd-1]

def changeVal(curr, brd, nx, ny) :
	"""
	이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
	0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
	"""
	if brd[nx][ny] == 0 :
		brd[nx][ny] = curr[6]
	else :
		curr[6] = brd[nx][ny]
		brd[nx][ny] = 0
	return curr, brd

def solve() :
	n, m, x, y, k = MIS()  # 세로길이, 가로길이, 시작x, 시작y, 명령 횟수
	brd = [[*MIS()] for i in range(n)]
	curr = [-1, 0, 0, 0, 0, 0, 0]  # 현재 주사위 상태

	for cmd in [*MIS()] :
		dx, dy = moving(cmd)
		nx, ny = x+dx, y+dy
		if nx < 0 or nx >= n or ny < 0 or ny >= m :
			continue
		curr = roll(curr, cmd) # 주사위가 범위를 초과하면 굴러가서도 안됨.
		curr, brd = changeVal(curr, brd, nx, ny)
		x, y = nx, ny
		print(curr[1])

if __name__ == "__main__" :
	solve()
