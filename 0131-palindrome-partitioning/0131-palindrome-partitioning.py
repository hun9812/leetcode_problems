class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        
        def findpal(k, cur_list):
            if k == len(s):
                self.res.append(cur_list[:])
                return
            cur_list.append(s[k])
            findpal(k+1, cur_list)
            cur_list.pop()

            rem = (len(s) - k) // 2
            for i in range(1, rem+1):
                for j in range(1,i+1):
                    if s[k+j-1] != s[k+(2*i)-j]:
                        break
                    if j == i:
                        cur_list.append(s[k:k+(2*i)])
                        findpal(k+(2*i),cur_list)
                        cur_list.pop()
                for j in range(1, i+1):
                    #print(i,j, cur_list, k)
                    if len(s) <= k+(2*i) or s[k+j-1] != s[k+(2*i)+1-j]:
                        break
                    if j == i:
                        cur_list.append(s[k:k+(2*i)+1])
                        findpal(k+(2*i)+1, cur_list)
                        cur_list.pop()
        
        findpal(0, [])
        return self.res