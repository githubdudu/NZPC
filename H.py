import math

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




def H():
    # input of four players
    t1p1 = io.getStrList()
    t1p2 = io.getStrList()
    t2p1 = io.getStrList()
    t2p2 = io.getStrList()
    isCompare = False

    t1min = min(int(t1p1[1]), int(t1p2[1]))
    t1max = max(int(t1p1[1]), int(t1p2[1]))

    t2min = min(int(t2p1[1]), int(t2p2[1]))
    t2max = max(int(t2p1[1]), int(t2p2[1]))


    
    if t1max < t2min:
        # 1, -5; 4, 2
        if int(t1p1[1]) < int(t1p2[1]):
            t1p1, t1p2 = t1p2, t1p1
        
        
        if int(t2p1[1]) < int(t2p2[1]):
            t2p1, t2p2 = t2p2, t2p1

        
        free = math.ceil((int(t2p1[1]) - int(t1p2[1])) / 2)
        if free == 0:
            print(f"No free turns between {t2p1[0]} and {t1p2[0]}")
        else:
            print(f"{t2p1[0]} receives {free} free turns from {t2p1[0]}")

        free = math.floor((int(t2p2[1]) - int(t1p1[1])) / 2)
        if free == 0:
            print(f"No free turns between {t2p2[0]} and {t1p1[0]}")
        else:
            print(f"{t1p1[0]} receives {free} free turns from {t2p2[0]}")


    if t2max < t1min:
        if int(t1p1[1]) < int(t1p2[1]):
            t1p1, t1p2 = t1p2, t1p1
        
        
        if int(t2p1[1]) < int(t2p2[1]):
            t2p1, t2p2 = t2p2, t2p1



        free = math.floor((int(t1p2[1]) - int(t2p1[1])) / 2)
        if free == 0:
            print(f"No free turns between {t2p1[0]} and {t1p2[0]}")
        else:
            print(f"{t1p2[0]} receives {free} free turns from {t2p1[0]}")

        free = math.ceil((int(t1p1[1]) - int(t2p2[1])) / 2)
        if free == 0:
            print(f"No free turns between {t1p1[0]} and {t2p2[0]}")
        else:
            print(f"{t1p1[0]} receives {free} free turns from {t2p2[0]}")

    else:
        pass

# # need to consider 0.5
#     t1weak_handy = (t2strong - t1weak)
#     t2weak_handy = (t1strong - t2weak)
#     if t1weak_handy % 2 == 1 and t2weak_handy % 2 == 1:
#         isCompare = True

#     t1weak_handy = t1weak_handy / 2.0
#     t2weak_handy = t2weak_handy / 2.0

#     if isCompare:
#         if t1weak_handy > t2weak_handy:
#             math.ceil(t1weak_handy)
#             math.floor(t2weak_handy)
#         elif t2weak_handy > t1weak_handy:
#             math.ceil(t2weak_handy)
#             math.floor(t1weak_handy)
#         else:
#             math.floor(t2weak_handy)
#             math.floor(t1weak_handy)
#         # else:
#         #     print(f"No free turns between {t1p1[0]} and {t1p2[0]}")
#     return

H()

