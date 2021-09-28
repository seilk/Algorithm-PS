# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(3))

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input().rstrip())
    dp = [0 for i in range(n + 1)]

    def fibo(n): #-> dp[n] = fibo(n - 1) + fibo(n - 2)
        if n == 1 or n == 2:
            dp[n] = 1
            return dp[n]
        if dp[n]:
            return dp[n]  # Using Memo
        dp[n] = fibo(n - 1) + fibo(n - 2)  # Memoization
        return dp[n]
    print(fibo(n))
