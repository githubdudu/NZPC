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

N, M = io.getIntList()
swt_configs = []

class swt:
    def __init__(self, s, w, t):
        self.s = s
        self.w = w
        self.t = t
    
    def __repr__(self) -> str:
        return str((self.s, self.w, self.t))


def problem():
    # Get configs
    for n in range(N):
        line = io.getIntList()

        config_n = []
        for i in range(0, len(line), 3):
            config_n.append(swt(line[i], line[i + 1], line[i + 2]))
        
        swt_configs.append(config_n)
    
    # where the 0th row is the northernmost.
    swt_configs.reverse()

    # make sure read
    # print(configs, N, M)

    # init dynamic array
    minutes = []
    for n in range(2 * N):
        minutes.append([-1] * 2 * M)
    # start node
    minutes[0][0] = 0;

    def findConfig(n, m):
        n = int((n - n % 1) / 2)
        m = int((m - m % 1) / 2)
        return swt_configs[n][m]
    
    def crossWE(conf, time):
        
        remainder = (time - conf.s - conf.t) % (conf.s + conf.w)
        if remainder >= 0 and remainder < conf.w:
            return time + 1;
        else:
            return time - remainder + conf.w + conf.s + 1

    def crossNS(conf, time):

        remainder = (time - conf.t) % (conf.s + conf.w)
        if remainder >= 0 and remainder < conf.s:
            return time + 1;
        else: 
            return time - remainder + conf.w + conf.s + 1
    def moveRight(n, m):
        if m % 2 == 0:
            # cross
            return crossWE(findConfig(n, m), minutes[n][m])
        else:
            # same block
            return minutes[n][m] + 2;
    def moveUp(n, m):
        if n % 2 == 0:
            # cross
            return crossNS(findConfig(n, m), minutes[n][m])
        else:
            # same block
            return minutes[n][m] + 2;
    def moveLeft(n, m):
        if m % 2 == 1:
            # cross
            return crossWE(findConfig(n, m - 1), minutes[n][m])
        else:
            # same block
            return minutes[n][m] + 2;
    def moveDown(n, m):
        if n % 2 == 1:
            # cross
            return crossNS(findConfig(n - 1, m), minutes[n][m])
        else:
            # same block
            return minutes[n][m] + 2;

    # main algo
    queue = [(0, 0)]
    while len(queue) > 0:
        def update(c, _n, _m):
            if c < minutes[_n][_m] or minutes[_n][_m] == -1:
                minutes[_n][_m] = c;
                queue.append((_n, _m))
        n, m = queue.pop(0);
        
        
        if m > 0:
            cost = moveLeft(n, m)
            update(cost, n, m - 1)
        if n > 0:
            cost = moveDown(n, m)
            update(cost, n - 1, m)
        if m < 2 * M - 1:
            cost = moveRight(n, m)
            update(cost, n, m + 1)
        if n < 2 * N - 1:
            cost = moveUp(n, m)
            update(cost, n + 1, m)

    # print(minutes) #commented out when submitting
    print(minutes[-1][-1])
problem()