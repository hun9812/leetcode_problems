class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        res = []
        if turnedOn > 8:
            return res
        if turnedOn == 0:
            return ["0:00"]
        
        minute = [1,2,4,8,16,32]
        hour = [1,2,4,8]
        
        for i in range(1, 1023):
            n = list(map(int, bin(i)[2:]))[::-1]
            if sum(n) != turnedOn:
                continue
            m = 0
            h = 0
            for j in range(len(n)):
                if j < 6:
                    if n[j] == 1:
                        m += minute[j]
                else:
                    if n[j] == 1:
                        h += hour[j-6]
            if m < 60 and h < 12:
                if m < 10:
                    res.append("{0}:0{1}".format(h, m))
                else:
                    res.append("{0}:{1}".format(h, m))
        return res





        
