import sys
# 재귀함수 사용하는 알고리즘에서는 습관처럼 setrecursion 잡아주자. 이거땜에 시간초과 남
sys.setrecursionlimit(10**7)

def find(x):
  if tree[x]!=x:
    tree[x]=find(tree[x])
  return tree[x]

def union(x,y):
  a=find(x)
  b=find(y)
  if a<b:
    tree[b]=a
  elif a>b:
    tree[a]=b

# fi = open("13306_tc.txt")
file = sys.stdin.readlines() # 입력 전체를 한꺼번에 받음 (최적화)
N, Q = [*map(int, file[0].split())] # 첫째 줄
tree = [i for i in range(N+1)]
ans = []

for f in file[N:][::-1]: # file의 n+1번째 라인부터 역순으로 확인함, 오버헤드 방지
  f=f.split()
  if int(f[0])==0:
    union(int(f[1]), int(file[int(f[1])-1])) # file의 순서상 노드 n의 부모노드는 file의 n-1번쨰 줄에 있음
  else:
    x,y=int(f[1]),int(f[2])
    if find(x)==find(y):
      ans.append("YES")
    else:
      ans.append("NO")

for a in ans[::-1]:
  print(a)