import sys
<<<<<<< HEAD
# n = 자리 개수 , m = 종료 개수, l = 받으면 던지는 위치
n, m, l = map(int, sys.stdin.readline().split())

# 공을 받는 횟수 저장
receive = [0 for i in range(n)]
receive[0] = 1

# while 문, 조건 : m in recieve, 공 던지는 횟수 초기화
=======
n, m, l = map(int, sys.stdin.readline().split())  #n = 자리 개수 , m = 종료 개수, l = 받으면 던지는 위치

#공을 받는 횟수 저장
receive = [0 for i in range(n)]; receive[0] = 1

#while 문, 조건 : m in recieve, 공 던지는 횟수 초기화
>>>>>>> temp2
throw = 0
i = 0
endgame = True
while endgame:

<<<<<<< HEAD
  # 홀수 = index ++
  if receive[i] % 2 != 0:
    i += l
    # index가 범위를 초과하는 경우
    if i > n - 1:
      receive[i - (n - 1) - 1] += 1
      i = i - (n - 1) - 1
    else:
      receive[i] += 1

  # 짝수 = index --
  elif receive[i] % 2 == 0:
    i -= l
    # index가 범위를 초과하는 경우
    if i < -n:
      receive[n + (i)] += 1
      i = n + (i)
    else:
      receive[i] += 1

  throw += 1

  if m in receive:
    endgame = False
=======
    #홀수 = index ++ 
    if receive[i] % 2 != 0:
        i += l
        # index가 범위를 초과하는 경우
        if i > n - 1:
            receive[i - (n - 1) - 1] += 1
            i = i - (n - 1) - 1
        else:
            receive[i] += 1
        
                   
    #짝수 = index --
    elif receive[i] % 2 == 0:
        i -= l
        #index가 범위를 초과하는 경우
        if i < -n:
            receive[n + (i)] += 1
            i = n + (i)
        else:
            receive[i] += 1

    throw += 1

    if m in receive:
        endgame = False
>>>>>>> temp2

print(throw)
