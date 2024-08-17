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


def K():
    T, M, S = io.getIntList()
    powerMap = [0] * (T + 1)
    hashMap = {}

    while True:
        a, t, p = io.getIntList()
        if [a, t, p] == [0, 0, 0]:
            break

        if a not in hashMap:
            hashMap[a] = t
        else:
            hashMap[a] += t

        powerMap[hashMap[a]] += p
    

    output = 0
    timeStamp = 0
    power = 0
    isInPeak = False

    for time, powerChange in enumerate(powerMap):
        # if time == (len(powerMap) - 1):
        #     break
        power += powerChange

        if power > M:
            if not isInPeak:
                timeStamp = time
                isInPeak = True
        else:
            if time - timeStamp <= S and time - timeStamp >= 1 and isInPeak:
                output += 1
                isInPeak = False

    print(output)
K()