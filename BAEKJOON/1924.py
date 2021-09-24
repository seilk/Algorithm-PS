x, y = map(int, input().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
accum_dates = sum(dates[:x-1]) + y
print(days[accum_dates % 7])

N = list(map(int, input().split()))
month = N[0]
date = N[1]
OneWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
if month == 1:
    date = date
else :         
    for i in range(1, month): #for문으로 날짜를 돌면서 이전 날짜~1월 까지의 총 일수를 더한다.
        if i == 2:
            date += 28
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            date += 31
        elif i in [4, 6, 9, 11]:
            date += 30
m = (date) % 7
print(OneWeek[m])