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
products = io.getStr()
line2 = io.getIntList()
pd, pc = line2[0], line2[1]

# er B which is the number of products that must be bought
# (from 2 to 150 inclusive) to get 1 free.
numToGetFree = io.getInt()

N = io.getInt()

def B():
    print(products)
    for n in range(N):
        num = io.getInt()

        gaps = [0]
        k = 1
        while gaps[-1] <= 200:
            gaps.append(numToGetFree * k)
            k += 1

        for i in range(len(gaps)):


            if num >= gaps[i] + i and num < gaps[i + 1] + i + 1:
                sum = num - i
    
                pcs = pc * i

                pds = pd * i + (pcs - pcs % 100) / 100

                pcs = pcs % 100

                print("Buy %s, pay for %d, get %d free. Save $%d.%.2d." % (num, sum, i, pds, pcs))
                break
B()