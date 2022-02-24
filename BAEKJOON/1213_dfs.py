import sys
def isPalindrome(wordlist):
    being = False
    for i in range(len(wordlist) // 2):
        if wordlist[i] == wordlist[len(wordlist) - 1 - i]:
            being = True
        else:
            being = False
            return being
    return being


def findPalindrome(depth):
    if depth == len(nameHansoo):
        if isPalindrome(tmp):
            print(*tmp, sep="")
            sorry = False
            sys.exit(0)
        return

    for i in range(len(nameHansoo)):
        if not dfs[i]:
            tmp.append(nameHansoo[i])
            dfs[i] = 1
            findPalindrome(depth + 1)
            tmp.pop()
            dfs[i] = 0

nameHansoo = list(input()); nameHansoo.sort()
dfs = [0 for i in range(len(nameHansoo))]
tmp = []; sorry = True
findPalindrome(0)
if sorry:
    print("I\'m Sorry Hansoo")

    