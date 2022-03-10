import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
sys.setrecursionlimit(10**5)
def rec(left, right, word, sig, length):
	if sig == 2: # 두 번 이상 다르면 팰린드롬이 될 수 없다고 판단.
		return 2
	if left > right :
		return sig
	if word[left] == word[right]:
		return rec(left + 1, right - 1, word, sig, length)
	else:
		# 한 번 다르면 시그널을 0 -> 1로 변경하고 recursion
		# 이 때 좌우 포인터를 한번씩 다 변경해봐야함
		# 2 또는 1이 return 될텐데 가능하면 1을 리턴하는게 맞으므로 min으로 리턴
		# 2, 2인 경우는 어떤 경우에서도 불가능하므로 2를 리턴
		return min(rec(left + 1, right, word, sig + 1, length), rec(left, right - 1, word, sig + 1, length))

N = int(In())
arr = [In() for i in range(N)]
for word in arr:
	l = len(word)
	print(rec(0, l - 1, word, 0, l))

