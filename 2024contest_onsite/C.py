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
length, width = io.getIntList()
M = io.getInt()

def C():
    hash = {}
    output = 0

    for m in range(M):
        x, y = io.getIntList()

        if (x, y) in hash:
            hash[(x, y)] += 1
        else:
            hash[(x, y)] = 1

    N = io.getInt()
    for n in range(N):
        x, y = io.getIntList()

        if (x, y) in hash:
            output += hash[(x, y)]

    print(output)   
C()