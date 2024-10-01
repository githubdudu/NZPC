class IO:
    def getStr(self):
        return input().strip()
    def getInt(self):
        return int(input().strip())
    def getStrList(self):
        return self.getStr().split(" ")
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    def strTuple(self, tuple):
        return "%s %s" % tuple
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()

T = io.getInt()  # 1e4

def problem_D():
    def sorted_idx(arr):
        return sorted(zip(arr, range(len(arr))))
    def conquer(arr, idxes):
        l, r = idxes[0][1], idxes[0][1]
        for v, idx in idxes:
            if idx >= l and idx <= r:
                continue
            elif idx < l:
                temp_diff = v - (r - idx + 1)
                if temp_diff >= 0:
                    l = idx
                else:
                    return False
            else:
                temp_diff = v - (idx - l + 1)
                if temp_diff >= 0:
                    r = idx
                else:
                    return False
        return True
    for _ in range(T):
        N = io.getInt()  # 2e5, 1e16
        An = io.getIntList()  # 1e10, len(An) == N

        ans = 0
        idxes = sorted_idx(An)
        
        found = conquer(An, idxes)
        if found:
            mn_i, mx_i = 0, N - 1
            for i in range(N):
                mn_i = max(mn_i, i - An[i] + 1)
                mx_i = min(mx_i, i + An[i] - 1)
            print(mx_i - mn_i + 1)
        else:
            print(0)

problem_D()