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

N = io.getInt()
valid = ["A", "B", "C", "D", "E", "F"]
def F():
    filteredOut = ""
    ansList = []

    for m in range(N):
        list = io.getStrList()
        newlist = []

        for ch in list:
            if ch.isnumeric() or ch in valid:
                newlist.append(ch)
            else:
                ansList.append(newlist)
                newlist = []
                filteredOut += ch
                
        if newlist != []:
            ansList.append(newlist)


    if filteredOut != "":    
        print(filteredOut)

    for newlist in ansList:
        if newlist == []: continue
        ans = 0
        for i, ch in enumerate(newlist):
            if ch.isnumeric():
                ch = int(ch)
            else:
                if ch == "A":
                    ch = 10
                elif ch == "B":
                    ch = 11
                elif ch == "C":
                    ch = 12
                elif ch == "D":
                    ch = 13
                elif ch == "E":
                    ch = 14
                elif ch == "F":
                    ch = 15
            ans += ch * 16 ** (len(newlist) - 1 - i)
        
        print(ans)

F()