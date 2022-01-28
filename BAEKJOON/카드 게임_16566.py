import sys
def find(idx):
  if check[idx] != -1:
    check[idx] = -1
    return idx, arr[idx]
  res, arr[idx] = find(arr[idx])
  return res, arr[idx]

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N, M, K = MIS()
MINSOO = [0]+[*MIS()]
CHEOLSOO = [*MIS()]
MINSOO.sort()
arr = [i+1 for i in range(M+1)]
arr[-1] = -1
check = [0]*(M+1)
for target in CHEOLSOO:
  start=1
  end=M
  while start<=end:
    mid=(start+end)//2
    if target<MINSOO[mid]:
      end=mid-1
      res=mid
    else:
      start=mid+1
  if check[res] == -1:
    x,tmp=find(res)
    print(MINSOO[x])
  else:
    check[res]=-1
    print(MINSOO[res])