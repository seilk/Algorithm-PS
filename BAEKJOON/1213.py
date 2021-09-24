import sys
nameHansoo = list(str(sys.stdin.readline().rstrip())); nameHansoo.sort()
spell_nameHansoo = list(set(nameHansoo)); spell_nameHansoo.sort() #중복 없는 리스트, Hansoo 이름에 포함된 알파벳으로 구성
# print(spell_nameHansoo)
save = [[0, 0] for i in range(len(spell_nameHansoo))]
for i in spell_nameHansoo:
    save[spell_nameHansoo.index(i)][0] = i #중복 없는 리스트에서 i의 위치가 2차리스트의 row가 된다.
    save[spell_nameHansoo.index(i)][1] = nameHansoo.count(i) #<<list>>.count("items")
save.sort() # [알파벳, 이름에 등장하는 횟수] 로 이뤄진 2차원 리스트 생성, 알파벳이 각 행의 첫번째 원소이므로 알파벳순으로 정렬
# print(save)
fault = 0 #홀수개인 알파벳의 개수 초기화
answer = "" #정답 초기화
center = "" #가운데 위치해야하는 알파벳 초기화
for i in range(len(save)): #i는 ABCD순으로 들어감 why? save.sort
    if save[i][1] % 2 == 1: #홀수인 경우
        fault += 1
        center = save[i][0] #홀수 덩어리가 무조건 가운데에 오게 되면 사전순을 위배함, 홀수값 자체를 저장
        if fault >= 2: #홀수개인 알파벳이 2개 이상이면 sorry hansoo 출력
            print("I\'m Sorry Hansoo", end = "")
            sys.exit(0)
    answer += save[i][0] * int(save[i][1] // 2) #홀수, 짝수 관계없이 알파벳에 몫만큼 곱해서 answer에 더해줌. (갱신) AA - > A         A

#알파벳 순으로 for loop을 돌기 때문에 가급적이면 들어오는 알파벳이 중간중간에 끼어있어야 답이 나온다.(사전순으로 첫번째 Palindrome)
#ZZZ가 있다고 하면 Z는 어차피 save의 마지막 원소가 되므로 답은 "...ZZZ..."가 된다. # AABBCC...VVXXZZZXXVV,,,CCBBAA
answer = answer + center + "".join(list(reversed(answer)))
print(answer)

#AAABB -> ABABA but BAAAB
#collections.Counter -> {items : # of items}

# # 팰린드롬 만들기
# import sys
# import collections

# inpuT = sorted(sys.stdin.readline().rstrip())
# dicT = collections.Counter(inpuT)

# odd = list(filter(lambda x:x[1]%2 == 1, dicT.items()))
# middle = ''

# if len(odd) > 1:
#   print("I'm Sorry Hansoo")
#   sys.exit(0)
# elif len(odd) == 1:
#   middle = odd[0][0]

# result = ''
# for key, val in dicT.items():
#     result += key*(val//2)

# print(result + middle + result[::-1])