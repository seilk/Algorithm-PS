import sys
sys.setrecursionlimit(10**4)
In = lambda:sys.stdin.readline().rstrip()


def isPal(word):
	return word == word[::-1]


def rec(word, l):
	global org
	if l==1:
		return "AKARAKA"

	if not isPal(word):
		return "IPSELENTI"
	if rec(word[ :l//2 ], l//2)=="IPSELENTI":
		return "IPSELENTI"
	return "AKARAKA"

org = list(In())
word = list(org)
print(rec(word, len(org)))
