S1 = input()
S2 = input()

def prob_I():
    for i in range(min(len(S1), len(S2))):
        if S1[i] == S2[i]:
            continue
        else:
            print(len(S1) + len(S2) - (i) * 2)
            return
    print(len(S1) + len(S2) - min(len(S1), len(S2)) * 2)
prob_I()