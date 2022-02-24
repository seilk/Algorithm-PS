# BOJ_주식_11501
# Tip : Greedy
# 가격이 이 전 날보다 오르기 전까지 매수하고 오르면 판다.
# import sys


# def buy(price):
#   global profits
#   global cnt
#   profits -= price
#   cnt += 1


# def sell(price):  # 한 번에 다 매도
#   global profits
#   global cnt
#   profits += price * cnt
#   cnt = 0


# def input(): return sys.stdin.readline().rstrip()


# ans = []
# tc = int(input())
# for case in range(tc):
#   days = int(input())
#   prices = [0] + list(map(int, input().split()))
#   maxx = prices[days]
#   profits = 0
#   for idx in range(days - 1, 0, -1):
#     if prices[idx] < maxx:
#       profits += maxx - prices[idx]
#     else:
#       maxx = prices[idx]
#   ans.append(profits)
# print(*ans, sep="\n")


# AC_CODE
# 분할 정복
# Tip : 최대 가격, 최대 가격의 인덱스를 저장하고 그 전까지의 day에는 주식을 사서 최대 가격인 날에 매도, 매도하고 그 다음날도 같은 방법 사용

import sys

def div_conq(c):
  max_index = 0
  max_cost = c[0]
  
  #max 업데이트
  for i in range(len(c)):
    if c[i] >= max_cost:
      max_index = i
      max_cost = c[i]
  
  # 최대가격 idx가 가장 마지막 날일때는 단순 계산 (전체 날짜 * 마지막 날의 가격 - 파는날을 제외한 날짜의 가격 sum)
  if max_index == len(c)-1:
    return (c[-1]*len(c)-sum(c))
  else: 
    # call recursion
    # 최대가격이 나오는 부분 계산
    # array를 slice해서 parameter로 전달
    return (c[max_index]*(max_index)-sum(c[:max_index])) + div_conq(c[max_index+1:])
  
#[111111111....111111] -> O(1_000_000) -> O(N)
#100만개 * O(N) 
#100만 * O(logN)
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
  n = int(sys.stdin.readline()[:-1])
  cost = list(map(int, sys.stdin.readline()[:-1].split()))
  print(div_conq(cost))

# Wrong Answer : 가장 비싼 시점에 매도 O, 가격이 오르면 전부 매도 X
# day = 1
# profits, cnt = 0, 0
# while day < days + 1:
#   if day < days:
#     # 다음날 가격이 오르는 경우
#     if prices[day] < prices[day + 1]:
#       buy(prices[day])

#     # 다음날 가격이 같은 경우
#     elif prices[day] == prices[day + 1]:
#       pass

#     # 다음날 가격이 떨어지는 경우
#     elif prices[day] > prices[day + 1]:
#       sell(prices[day])

#   else:  # 마지막날
#     sell(prices[day])

#   day += 1

# import bisect
# lst = [2, 2, 3, 4]
# n =bisect.bisect_left(lst, 1)
# print(n)