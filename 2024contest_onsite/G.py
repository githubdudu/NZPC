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


def G():
    dragons, knights = io.getIntList()
    dragonList, knightList = [], []
    for _ in range(dragons):
        dragonList.append(io.getInt())
    for _ in range(knights):
        knightList.append(io.getInt())
    dragonList.sort()
    knightList.sort()

    d, k = 0, 0
    cost = 0

    while d < len(dragonList) and k < len(knightList):
        if dragonList[d] > knightList[k]:
            k += 1
        else:
            cost += knightList[k]
            d += 1
            k += 1
    
    if d == len(dragonList):
        print(cost)
    else:
        print("Loowater is doomed!")

G()