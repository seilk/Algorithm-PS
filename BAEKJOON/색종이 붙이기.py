import sys

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def paper(cmd, cy, cx, brd) :
	needs = 0
	if cx+cmd>10 or cy+cmd>10 :
		return False

	for i in range(cy, cy+cmd) :
		for j in range(cx, cx+cmd) :
			if brd[ i ][ j ] == 0 :
				return False
	return True

def attach(cy, cx, cmd) :
	for i in range(cy, cy+cmd) :
		for j in range(cx, cx+cmd) :
			brd[ i ][ j ] = 0

def detach(cy, cx, cmd) :
	for i in range(cy, cy+cmd) :
		for j in range(cx, cx+cmd) :
			brd[ i ][ j ] = 1

def btrk(cy, cx, used, brd, paperNums) :
	global ans
	if cy>=10:
		ans = min(ans, used)
		return

	if cx>=10 :
		btrk(cy+1, 0, used, brd, paperNums)
		return

	if brd[ cy ][ cx ] == 1 :
		for cmd in range(5, 0, -1) :
			if paperNums[ cmd ]<=0 : continue
			if paper(cmd, cy, cx, brd) :
				attach(cy, cx, cmd)
				paperNums[ cmd ] -= 1
				btrk(cy, cx+1, used+1, brd, paperNums)
				detach(cy, cx, cmd)
				paperNums[ cmd ] += 1
	else :
		btrk(cy, cx+1, used, brd, paperNums)

brd = [ [ *MIS() ] for i in range(10) ]
ans = 1e9
btrk(0, 0, 0, brd, [ 0, 5, 5, 5, 5, 5 ])
print(-1 if ans == 1e9 else ans)
