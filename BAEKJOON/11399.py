from sys import stdin
#기다리는 시간은 누적이 되기 때문에 빨리 끝나는 사람이 먼저 해야함.
n = int(stdin.readline().rstrip())
time = list(map(int, stdin.readline().split()))
time.sort()

#개인별 걸리는 시간을 구하고 따로 list에 저장해둠
#마지막에 list의 모든 items를 합침
time_person = time[0]
time_total =[time[0]]
for i in range(1, n):
    time_person += time[i]
    time_total.append(time_person)
print(sum(time_total))