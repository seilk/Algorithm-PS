import sys

def cal() :
	ret = 0
	for i in range(n) :
		word = wordTerms[i]
		num = 0
		l = len(word)
		for j in range(l) :
			num += match[indices[word[j]]]*(10**(l-j-1))
		ret += num
	return ret

def rec(depth) :
	global ans, vist_num, match
	if depth == tot :
		ans = max(ans, cal())
		return

	for i in range(9, -1, -1) :
		if vist_num[i] == 1 : continue
		vist_num[i] = True
		match[depth] = i
		rec(depth+1)
		vist_num[i] = False

def solve() :
	global wordTerms, n, words, tot, match, vist_num, ans, indices
	n = int(sys.stdin.readline().rstrip())
	wordTerms = []
	words = set()
	for _ in range(n) :
		wordTerms.append(list(sys.stdin.readline().rstrip()))
		for w in wordTerms[-1] :
			words.add(w)

	tot = len(words)
	words = list(words)

	indices = { val : idx for idx, val in enumerate(words) }
	match = [-1 for i in range(tot)]
	vist_num = [False]*10
	ans = 0
	rec(0)
	print(ans)

if __name__ == "__main__" :
	solve()
