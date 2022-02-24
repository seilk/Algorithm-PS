def solution(N, number):
    # dp[i]에는 N을 i번 사용하는 연산들의 집합을 저장함.
    # 중복을 피하는 set함수를 이용함.
    # 8번을 사용해서 만들지 못하면 -1을 출력하므로 item의 개수는 8개로도 충분함.
    dp = [set() for i in range(9)]
    # i번째 set에는 N을 i번 사용한 숫자를 무조건 포함
    
    dp[1].add(N)
    if number == N:
        return 1
    for i in range(2, 9):
        dp[i].add(int(str(N) * i))
        # i번째 set은 N을 i번 사용한 연산임
        # N을 i번 사용한 연산은 
            # N을 1번 사용한 연산 + N-1번 사용한 연산   
            # N을 2번 사용한 연산 + N-2번 사용한 연산
            # .... N을 N/2번 사용한 연산 + N/2번 사용한 연산
            # 그 이상은 앞서 과정에서 중복됨.
        # j는 첫번째 연산할 set을 결정 (1부터 N/2까지)
        for j in range(1, i//2 + 1):
            # N - j 로 생각하고 for문 안씀
            # set안에 있는 값들을 지정해야함
            for k in dp[j]:
                for t in dp[i - j]:
                    dp[i].add(k + t)
                    dp[i].add(k - t)
                    dp[i].add(k * t)
                    if k != 0:
                        dp[i].add(t // k)
                    if t != 0:
                        dp[i].add(k // t)
                    if number in dp[i]:
                        return i
    return - 1

print(solution(5, 12))