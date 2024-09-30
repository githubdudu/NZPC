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
def problem_A():
    diction = {}
    # def dp(i, arr, L):
    #     if i >= L:
    #         return 0, 0
        
    #     nextMax = max(dp(i + 2, arr, L), dp(i + 3, arr, L))
    #     diction[i] = arr[i] + nextMax
    #     return diction[i]

    for _ in range(T):
        N = io.getInt()
        list_a = io.getIntList();
        max_even = 0
        max_odd = 0
        for i in range(len(list_a)):
            if i % 2 == 0:
                max_odd = max(max_odd, list_a[i])
            else:
                max_even = max(max_even, list_a[i])
        len_even = len(list_a) // 2
        len_odd = len(list_a) - len_even
        print(max(max_even + len_even, max_odd + len_odd))


problem_A()