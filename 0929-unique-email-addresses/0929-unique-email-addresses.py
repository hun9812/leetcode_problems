class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        dict = {}
        
        for i in emails:
            temp = ""
            at = False
            j = 0
            while j < len(i):
                if i[j] == "@":
                    at = True
                    temp += "@"
                    j += 1
                elif i[j] == "+":
                    if at is True:
                        temp += "+"
                        j += 1
                        continue
                    while i[j] != "@":
                        j += 1
                    at = True
                    temp += "@"
                    j += 1
                elif i[j] == ".":
                    if at:
                        temp += i[j]
                        j += 1
                    else:
                        j+=1
                        continue
                else:
                    temp += i[j]
                    j+=1
            
            print(temp)
            if temp in dict:
                continue
            else:
                dict[temp] = True
                res += 1
        
        return res
        