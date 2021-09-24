from sys import stdin
t = int(stdin.readline().rstrip())
for i in range(t):
    numberofWords = int(stdin.readline().rstrip())
    note = []
    beingPalindrome = False
    for j in range(numberofWords):
        note.append(str(stdin.readline().rstrip()))

    for j in range(numberofWords):
        if beingPalindrome:
            break
        for k in range(numberofWords):
            if j == k:
                continue
            isPalindrome = list(note[j] + note[k])
            if isPalindrome == list(reversed(isPalindrome)) :
                print(*isPalindrome, sep="")
                beingPalindrome = True
                break
    if not beingPalindrome:                
        print(0)
## 반 접어서 확인하는 방법이 있음.
# i = "apple"
# print(i[:3])
# print(i.sort(reverse = True)) 