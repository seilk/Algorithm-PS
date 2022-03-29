import sys

In = lambda:sys.stdin.readline().rstrip()
MIS = lambda:map(int,In().split())


def command(i):
	# ascii 순서로 정렬
	if i==0:
		return " "
	if i==1:
		return "+"
	if i==2:
		return "-"


def func(n,arr,depth,idx):
	global ans
	if depth==n-1:
		ret = eval("".join(arr).replace(" ","")) # "1+2+3" -> 6
		if ret==0:
			ans.append("".join(arr))
		return

	for c in range(3):  # 0, 1, 2 = " ", +, -
		arr[idx] = command(c)
		func(n,arr,depth+1,idx+2)
		arr[idx] = ""


t = int(In())
for _ in range(t):
	n = int(In())
	ans = [ ]
	arr = [ "" for i in range(2*n-1) ]
	num = 1
	for i in range(0,2*n-1,2):
		arr[ i ] = str(num)
		num += 1
	func(n,arr,0,1)
	print(*ans,sep="\n")
	print()
