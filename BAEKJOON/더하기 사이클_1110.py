import sys
N = int(sys.stdin.readline().rstrip())
lst = list(str(N))
if N < 10:
    lst.insert(0, '0')
#lst = ['n', 'm']

number = int(lst[0]) + int(lst[1])
tmp = [lst[1], str(number % 10)]
cycle = 1
while tmp != lst:
    number = 0
    for i in range(2):
        number += int(tmp[i])
    tmp[0] = tmp[1]
    tmp[1] = str(number % 10)
    cycle += 1
print(cycle) 

'''
a = ['1', '2']
print(a == ['1', '2'])
b = 12
print(list(str(b)))
'''