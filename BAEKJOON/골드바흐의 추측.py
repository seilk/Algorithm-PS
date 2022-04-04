import sys

def filterPrime() :
	vist = [0]*10001
	for i in range(2, 10001) :
		k = 2
		while i*k < 10001 :
			vist[i*k] = 1
			k += 1
	return [i for i in range(1, 10001) if vist[i] == 0]

t = int(sys.stdin.readline().rstrip())

primes = filterPrime()

sup = [[0,0] for i in range(primes[-1] + primes[-1] + 1)] # 테스트케이스를 대비한 전처리
diff = [10001] * (primes[-1] + primes[-1] + 1)
for i in range(1230):
	for j in range(i, 1230):
		num = primes[i] + primes[j]
		if diff[num] > abs(primes[i] - primes[j]):
			diff[num] = abs(primes[i] - primes[j])
			sup[num] = [primes[i], primes[j]]

for _ in range(t) :
	ans = [0, 0]
	ansDiff = 10001
	n = int(sys.stdin.readline().rstrip())
	print(*sup[n])
