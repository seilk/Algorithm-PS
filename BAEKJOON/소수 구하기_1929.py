m,n=map(int,input().split())
*l,=range(n+1)
for i in l[2:]:
	if l[i]>=m:print(i)
	l[i::i]=n//i*[0]
	# i 부터 끝까지 i 간격으로 https://blog.wonkyunglee.io/3
	# 슬라이싱을 통해 새로운 배열을 할당하면 원본 배열에서 슬라이싱 한 부분만 새로운 배열로 바뀜