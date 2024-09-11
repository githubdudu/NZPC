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

N = io.getInt()
machines = io.getStr()

coffee = 0
output = 0
for machine in machines:
    if machine == '1':
        output += 1
        coffee = 2
    else:
        if coffee:
            output += 1
            coffee -= 1


    
print(output)