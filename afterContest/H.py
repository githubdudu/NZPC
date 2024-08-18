import math

class IO():
    def getStr(self):
        return input().strip()
    
    def getInt(self):
        return int(input().strip())
    
    def getStrList(self):
        return self.getStr().split(' ')
    
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    
    def strTuple(self, tuple):
        return "%s %s" % tuple
    
    def strList(self, li):
        return " ".join(map(str, li))
io = IO() 

class team():
    def __init__(self, x, y) -> None:
        self.strong, self.weak = self.compare(x, y)
    def compare(self, x, y):
        if y.weaker(x) or x.same(y):
            return x, y
        else:
            return y, x
    
class player():
    def __init__(self, li) -> None:
        self.name = li[0]
        self.score = int(li[1])
    def weaker(self, that):
        return self.score > that.score
    def same(self, that):
        return self.score == that.score

def H():
    # input of four players
    p1 = player(io.getStrList())
    p2 = player(io.getStrList())
    team1 = team(p1, p2)
    p1 = player(io.getStrList())
    p2 = player(io.getStrList())
    team2 = team(p1, p2)

    free1 = -1
    free2 = -1
    ft1 = abs(team1.strong.score - team2.weak.score)
    ft2 = abs(team1.weak.score - team2.strong.score)
    if team1.strong.weaker(team2.weak) and ft1 % 2 == 1:
        free1 = 1
    else:
        free1 = 2
    if team2.strong.weaker(team1.weak) and ft2 % 2 == 1:
        free2 = 2
    else:
        free2 = 1

    ft1 = (ft1 + ft1 % 2) / 2
    ft2 = (ft2 + ft2 % 2) / 2

    if free1 == free2 and free1 == 1:
        ft1 -= 1
    elif free1 == free2 and free1 == 2:
        ft2 -= 1

    # display
    if ft1 == 0:
        print(f"No free turns between {team2.weak.name} and {team1.strong.name}.")
        
    else:
        print(f"{team2.weak.name} receives {int(ft1)} free turns from {team1.strong.name}.")

    if ft2 == 0:
        print(f"No free turns between {team1.weak.name} and {team2.strong.name}.")
        
    else:
        print(f"{team1.weak.name} receives {int(ft2)} free turns from {team2.strong.name}.")
H()
# 0min
