n = int(input())

arr = [input() for i in range(n)]
alpha = set()
for word in arr:
    for ch in word:
        alpha.add(ch)

alpha = list(alpha)
length = len(alpha)

visited = [False for i in range(10)]
match = [-1 for i in alpha]
maximum = 0

def dfs(index):
    global visited,maximum,match
    if index == length:
        total = 0
        for word in arr:
            add = 0
            for c in word:
                x = alpha.index(c)
                x= match[x]
                add = add*10+x
            total +=add
        maximum = max(maximum,total)
        return

    for j in range(10):
        if not visited[j]:
            visited[j] = True
            match[index] = j
            dfs(index + 1)
            visited[j] = False


dfs(0)
print(maximum)