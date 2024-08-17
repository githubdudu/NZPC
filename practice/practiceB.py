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

answer = io.getInt()
currWinner = ["", float("inf")]
for i in range(io.getInt()):
    currPerson = io.getStr()
    currGuess = io.getInt()
    if abs(answer - currGuess) < abs(currWinner[1] - answer):
        currWinner = [currPerson, currGuess]
print(currWinner[0])