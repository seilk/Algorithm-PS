import sys
from sys import stdin
n, k = map(int, stdin.readline().split())
tall = list(map(int, stdin.readline().split()))
group = [[] for i in range(k)]
g = 0
for i in range(n - 1, -1, -1):
    if k == 1:
        print(max(tall) - min(tall))
        sys.exit()
        break
    if k == n:
        print(0)
        sys.exit()
        break

    g += 1
<<<<<<< HEAD
    if g <= k:  # group에 빈 리스트가 없을 때
        group[(n - i) - 1].append(tall[i])
    else:
        # group의 가장 마지막 값의 첫번째 요소와 새로 추가되는 tall의 값.
        diffmin = abs(group[k - 1][0] - tall[i])
        tmp = [diffmin, k]  # group의 요소들을 바꿔주기 위해서 가장 작은 차이, 인덱스를 임시로 저장.
        for j in range(k - 1, -1, -1):
            if len(group[j]) == 1:
                diffmin = min(diffmin, (abs(group[j][0] - group[j - 1][0])))

            else:
                diffmin = min(
                    diffmin, (abs(group[j][0] - group[j - 1][0]) + abs(group[k - 1][1] - tall[i])))
            tmp[0] = diffmin
            99
            tmp[1] = j

        if tmp[1] == k:  # not changed
=======
    if g <= k: #group에 빈 리스트가 없을 때
        group[(n - i) - 1].append(tall[i])
    else:
        diffmin = abs(group[k - 1][0] - tall[i]) #group의 가장 마지막 값의 첫번째 요소와 새로 추가되는 tall의 값.
        tmp = [diffmin, k] #group의 요소들을 바꿔주기 위해서 가장 작은 차이, 인덱스를 임시로 저장.
        for j in range(k - 1, -1 ,-1):
            if len(group[j]) == 1:
                diffmin = min(diffmin, (abs(group[j][0] - group[j - 1][0])))

            else : 
                diffmin = min(diffmin, (abs(group[j][0] - group[j - 1][0]) + abs(group[k - 1][1] - tall[i])))
            tmp[0] = diffmin;
            tmp[1] = j

        if tmp[1] == k: # not changed
>>>>>>> temp2
            group[k - 1].append(tall[i])
        else:
            if len(group[tmp[1]]) == 2:
                group[tmp[1] - 1].append(group[tmp[1]].pop(0))
<<<<<<< HEAD
                group.sort(reverse=True)
                group[k - 1].append(tall[i])

            else:
                group[tmp[1] - 1].append(group[tmp[1]].pop(0))
                group.sort(reverse=True)
=======
                group.sort(reverse = True)
                group[k - 1].append(tall[i])
    
            else:
                group[tmp[1] - 1].append(group[tmp[1]].pop(0))
                group.sort(reverse = True)
>>>>>>> temp2
                group[k - 1].append(tall[i])

price = 0
for i in range(k):
    price += abs(group[i][0] - group[i][-1])
print(price)
<<<<<<< HEAD


=======
        
            
>>>>>>> temp2
# lst = [[1], [3,4]]
# a = lst[0].pop(0)
# lst.append(lst.pop(0))
# print(lst)
# print(a)
