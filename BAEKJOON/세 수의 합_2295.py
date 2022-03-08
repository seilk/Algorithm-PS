import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

if __name__ == "__main__":
	N = int(In())
	arr = [int(In()) for i in range(N)]
	team = []
	for i in range(N):
		for j in range(N):
			team.append(arr[i] + arr[j])
	
	team.sort()
	ans = -1
	for r in range(N):
		for z in range(N):
			if arr[r] - arr[z] <= 0 : continue
			target = arr[r] - arr[z]
			left = 0
			right = N**2
			while left <= right:
				mid = (left + right) // 2
				if team[mid] < target:
					left = mid + 1
				elif team[mid] == target:
					ans = max(ans, arr[r])
					break
				else:
					right = mid - 1
	print(ans)
	
'''
arr[x] + arr[y] + arr[z] = arr[r] 인 x,y,z,r에서
arr[r]이 최대인 값을 찾아라
x,y,z,r이 서로 같아도 된다.
풀이1 : 나이브하게 네 개의 인덱스를 각각 찾는다. N^4
풀이2 : 세 개의 인덱스를 모으고 arr[r]을 이분탐색으로 찾는다. N^3logN

근데 위 풀이들이 N이 최대 1000개라서 시간제한에 걸린다.

N^2logN으로 푸는 방법이 있다.
풀이3 : team 배열을 하나 만든다.
team 배열에는 arr[x] + arr[y]가 들어간다.
team[t] + arr[z] = arr[r]인 t,z,r을 구하면 된다.
식을 조금 변형해보면
team[t] = arr[r] - arr[z] 가 되고
이제 r과 z를 찾아주고 그 값이 team 배열에 있는 값인지 아닌지를 확인해주면 된다.
-> N^2logN
'''
			
			