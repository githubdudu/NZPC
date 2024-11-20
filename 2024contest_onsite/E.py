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


def E():

    while True:
        number = io.getStr()
        sum = 0

        if number == "0":
            break

        # first sum
        for i in range((len(number))):
            sum += int(number[i]) * (len(number) + 1 - i)

        # 
        rmd = 11 - sum % 11
        if rmd >= 1 and rmd <= 9:
            ans = number + str(rmd)
        elif rmd == 11:
            ans = number + "0"
        elif rmd == 10:
            ans = "rejected"
        print(f"{number} -> {ans}")

E()

# output
print()