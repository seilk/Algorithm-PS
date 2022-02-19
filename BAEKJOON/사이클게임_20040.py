# 유니온 파인드로 사이클을 찾는 문제.
# point : 입력을 받을때 마다 확인해줘야 함.

import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(x):
  if grp[x] == x:
    return x
  grp[x]=find(grp[x])
  return grp[x]

def union(x,y):
  a=find(x)
  b=find(y)
  if a<b:
    grp[b]=a
  else:
    grp[a]=b

n, m = MIS()
grp = [i for i in range(n)] # 인덱스를 값으로 갖게끔 초기화
flg=False
ans=0
for i in range(1,m+1):
  a,b=MIS()
  if flg:continue
  if find(a)==find(b):
    print(i)
    sys.exit(0)
  else:
    union(a,b)
print(ans)