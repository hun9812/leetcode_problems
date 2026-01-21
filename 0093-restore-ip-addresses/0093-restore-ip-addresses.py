class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []

        def make_ip_address(start, cur):
            #print(start, cur)
            if len(cur) == 4:
                if start == len(s):
                    self.res.append(".".join(cur))
                else:
                    return
            
            if start >= len(s) or len(cur) > 4:
                return
            
            if len(s)-start > (4-len(cur))*3:
                return
            
            if start+1 <= len(s):
                cur.append(s[start])
                make_ip_address(start+1, cur)
                cur.pop()
            if s[start] != "0":
                if start+2 <= len(s):
                    cur.append(s[start:start+2])
                    make_ip_address(start+2, cur)
                    cur.pop()
                if start+3 <= len(s) and int(s[start:start+3]) <= 255:
                    cur.append(s[start:start+3])
                    make_ip_address(start+3, cur)
                    cur.pop()
        
        make_ip_address(0, [])
        return self.res
        