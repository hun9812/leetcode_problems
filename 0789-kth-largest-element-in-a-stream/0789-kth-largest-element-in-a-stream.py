class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        self.nums = self.nums[-k:]
        return
        

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
            if len(self.nums) == self.k:
                return self.nums[0]
            else:
                return
        if val > self.nums[0]:
            self.nums.append(val)
            self.nums.sort()
            self.nums = self.nums[1:]
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)