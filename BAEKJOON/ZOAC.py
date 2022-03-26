import sys

In = lambda:sys.stdin.readline().rstrip()
word = list(In())
wordWithIndex = [ (val,i) for i,val in enumerate(word) ] #
wordWithIndex.sort()
l = len(word)
ret = [ "" for i in range(l) ] #["" "" "" ""]
vist = [ 0 ]*l
cur = wordWithIndex[ 0 ][ 0 ] #철자
vist[ wordWithIndex[ 0 ][ 1 ] ] = 1
ret[ wordWithIndex[ 0 ][ 1 ] ] = cur
ans = [ cur ]
d = 1
while d < l:
	semi = [ ]
	for val,i in wordWithIndex:
		if vist[ i ]==1: continue
		ret[ i ] = val
		semi.append(("".join(ret),val,i))
		ret[ i ] = ""
	cur,min_val,min_idx = min(semi)
	ans.append(cur)
	vist[ min_idx ] = 1
	ret[ min_idx ] = min_val
	d += 1

print(*ans,sep="\n")

'''
ZOAC
ACOZ

A
AC
OAC
ZOAC
'''
'''
BAC

ABC
A
BA
ABC
'''