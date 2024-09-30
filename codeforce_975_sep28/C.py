class IO:
    def getStr(self):
        return input().strip()

    def getInt(self):
        return int(input().strip())

    def getStrList(self):
        return self.getStr().split(" ")

    def getIntList(self):
        return [int(x) for x in self.getStrList()]

    def strTuple(self, tuple):
        return "%s %s" % tuple

    def strList(self, li):
        return " ".join(map(str, li))


io = IO()

T = io.getInt()  # 1e4


def canbuy(money, sum_cards, height, max_l):
    remainder = (height - sum_cards % height) % height

    if max_l * height > sum_cards + money:
        return False
    elif remainder > money:
        return False
    else:
        return True


def problem_C():
    for _ in range(T):
        N, K = io.getIntList()  # 2e5, 1e16
        An = io.getIntList()  # 1e10, len(An) == N

        An.sort()
        MAX_L = max(An)
        sum_cards = sum(An)

        while True:
            if canbuy(K, sum_cards, N, MAX_L):
                print(N)
                break
            elif N == 1:
                print(1)
                break
            N -= 1
        

problem_C()

# output
print()
