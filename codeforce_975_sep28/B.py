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

T = io.getInt()

def helper(N, Q, coors, queries):
    counts = {}

    # the n points that in the test case
    for i in range(N):
        # segment that end with i or begin with i
        count = N - 1 
        # segment that contains i
        count += i * (N - i - 1)
        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 1

    # rest of the points that not in the test case
    for i in range(N - 1):
        count = (i + 1) * (N - i - 1) 
        howmany = (coors[i + 1] - coors[i] - 1)
        if count in counts:
            counts[count] += howmany
        else:
            counts[count] = howmany
    output = []
    # 
    for q in queries:
        if q in counts:
            output.append(counts[q])
        else:
            output.append(0)
    print(*output)

def problem_B():
    for _ in range(T):
        N, Q = io.getIntList()
        coors = io.getIntList()
        queries = io.getIntList()
        helper(N, Q, coors, queries)

problem_B()