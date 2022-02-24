import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

if __name__=="__main__":
  N = int(In())
  k = int(In()) # 오름차순으로 정렬했을 때 B의 k번째 수를 구하라
  lo, hi = 1, N*N # N*N이 최대 100억이므로 arr을 할당할 수 없음 bisect는 사용하지 못함
  while lo<=hi:
    mid = (lo+hi)//2
    c=0
    for i in range(1,N+1):
      c+=min((mid//i),N)
      if i>mid:break
    if k <= c:
      hi=mid-1
      ans=mid # mid 보다 작은 수가 적어도 k개 이상 있다는 의미. 값을 저장하고 이후 과정을 탐색함.
    else:
      lo=mid+1
  print(ans)