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

def isLeap(year):
    if year % 400 == 0:
        return 'leap'
    if year % 4 == 0 and year % 100 != 0:
        return "leap"
    return 'common'

def time(year):
    if year == 2024:
        return "is"
    if year < 2024:
        return "was"
    if year > 2024:
        return "will be"

N = io.getInt()
def A():
    for i in range(N):
        year = io.getInt()
        print(f"{year} {time(year)} a {isLeap(year)} year.")
A()