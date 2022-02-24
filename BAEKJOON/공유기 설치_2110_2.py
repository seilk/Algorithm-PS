import sys

input = sys.stdin.readline
N, C = map(int, input().split())
coo = [int(input().rstrip()) for i in range(N)]
coo.sort()  # NlogN
start = 1  # 최소 인접거리
end = coo[-1] - coo[0]  # 최대 인접거리
ans = 1
while start <= end:
  mid = (start + end) // 2
  cnt = 1  # 맨 처음 좌표에 1개 설치하고 시작
  cur = 0
  for h in range(1, N):
    if mid <= coo[h] - coo[cur]:
      cnt += 1
      cur = h
  if cnt < C:
    end = mid - 1
  else:
    start = mid + 1
    ans = max(ans, mid)
print(ans)
