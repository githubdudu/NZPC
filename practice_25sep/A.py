N = int(input())

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

isEnd = False
count = 0

def dfs(name, isVowelNext):
    global count
    if count == N:
        return
    if len(name) > 20:
        return
    
    if len(name) > 3:
        print(name)
        count += 1

    if isVowelNext:
        for v in vowels:
            dfs(name + v, False)
    else:
        for c in consonants:
            dfs(name + c, True)


dfs('', True)