class IO():
    def getStr(self):
        return input().strip()
    
    def getInt(self):
        return int(input())
    
    def getStrList(self):
        return self.getStr().split(' ')
    
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    
    def strTuple(self, tuple):
        return "%s %s" % tuple
    
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()        


# input


def D():
    li = []

    score = 0
    output = []
    temps = []

    for n in range(8):
        temp = io.getStr()
        temps.append(temp)
        li.append(temp.split(" v "))



    for n in range(8):
        line = io.getIntList()

        if line[0] != line[1]:
            score += 1
        elif line[0] == 0:
            score += 2
        else:
            output.append(temps[n])
            score += 3
    
    print(f"Points scored: {score}")

    if output == []:
        print("No scoring draws")
    else:
        for s in output:
            print(s)
D()