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

    # Tag if there are half turns
    if team1.strong.weaker(team2.weak) and ft1 % 2 == 1:
        free1 = 1
    elif team2.weak.weaker(team1.strong) and ft1 % 2 == 1:
        free1 = 2
    if team2.strong.weaker(team1.weak) and ft2 % 2 == 1:
        free2 = 2
    elif team1.weak.weaker(team2.strong) and ft2 % 2 == 1:
        free2 = 1

    ft1 = (ft1 + ft1 % 2) / 2 # round up
    ft2 = (ft2 + ft2 % 2) / 2 # round up

    # Balance the half turns if same team have half turns
    if free1 == free2 and free1 == 1:
        ft1 -= 1
    elif free1 == free2 and free1 == 2:
        ft2 -= 1


    weaker = None
    stronger = None
    # display
    if ft1 == 0:
        print(f"No free turns between {team2.weak.name} and {team1.strong.name}.")
    
    else:
        if team2.weak.weaker(team1.strong):
            weaker = team2.weak
            stronger = team1.strong
        else:
            weaker = team1.strong
            stronger = team2.weak

        print(f"{weaker.name} receives {int(ft1)} free {'turn' if int(ft1) == 1 else 'turns'} from {stronger.name}.")

    if ft2 == 0:
        print(f"No free turns between {team1.weak.name} and {team2.strong.name}.")
        
    else:
        
        if team1.weak.weaker(team2.strong):
            weaker = team1.weak
            stronger = team2.strong
        else:
            weaker = team2.strong
            stronger = team1.weak

        print(f"{weaker.name} receives {int(ft2)} free {'turn' if int(ft2) == 1 else 'turns'} from {stronger.name}.")
H()
# 0min
