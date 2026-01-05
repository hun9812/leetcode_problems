class RecentCounter:

    def __init__(self):
        self.ping_list1 = []
        self.ping_list2 = []
        

    def ping(self, t: int) -> int:
        check = t - 3000
        count = 1
        if len(self.ping_list2) == 0:
            self.ping_list2.append(t)
            while self.ping_list1:
                temp = self.ping_list1.pop()
                if temp < check:
                    break
                else:
                    count += 1
                    self.ping_list2.append(temp)
            self.ping_list1 = []
            return count
        else:
            while self.ping_list2:
                temp = self.ping_list2.pop()
                if temp < check:
                    continue
                else:
                    count += 1
                    self.ping_list1.append(temp)
            self.ping_list1.append(t)
            self.ping_list2 = []
            return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)