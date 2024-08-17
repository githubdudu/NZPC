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


def C():

    while True:
        line = io.getStrList()
        balance = int(line[0])
        action = line[1]
        amount = int(line[2])

        if line == ['0', "W", "0"]:
            break

        if action == "W":
            balance -= amount
        else:
            balance += amount
        if balance < -200:
            print("Not allowed")
        else:
            print(balance)

C()

# output
print()