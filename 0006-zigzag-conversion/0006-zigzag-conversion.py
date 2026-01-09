class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # row가 3개면 하나 완성하는데 4개, row가 4면 6개: 2n-2
        # row1 => 0 , 2n-2, 2(2n-2)
        # row2 =>
        # rown => n-1, n-1 + 2n-2, n-1 + 2(2n-2)
        if len(s) == 1:
            return s
        if numRows == 1:
            return s
        output = ""

        for i in range(numRows):
            temp = 0
            if i == 0:
                while temp < len(s):
                    output += s[temp]
                    temp += (2*numRows - 2)
            elif i == numRows-1:
                temp = numRows-1
                while temp < len(s):
                    output += s[temp]
                    temp += (2*numRows - 2)
            else:
                temp = 0
                while temp <= len(s):
                    if temp+i < len(s):
                        output += s[temp+i]
                    if temp+(2*numRows-2)-i < len(s):
                        output += s[temp+(2*numRows-2)-i]
                    temp += (2*numRows - 2)
            print(i, output)
        
        return output
        