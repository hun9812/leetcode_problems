class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 / 1 / 10 / 11 / 100 / 101 / 110 / 111 / 1000 / 1001 / 1010 / 1011/ 1100 / 1101 / 1110 / 1111
        # 10000 / 10001 / 10010 / 10011 / 10100 / 10101 / 10110 / 10111 / 11000 / 11001
        # 11010 / 11011 / 11100 / 11101 / 11110 / 11111 / 100000
        # 0, 1, 1 2, 1 2 2 3, 1 2 2 3 2 3 3 4, 1 2 2 3 2 3 3 4 2 3 3 4 3 4 4 5,  
        # 131072 17
        cnt = 1
        arr = [0, 1]
        while cnt < 100000:
            for i in range(cnt, cnt*2):
                arr.append(arr[i])
            for i in range(cnt, cnt*2):
                arr.append(arr[i] + 1)
            cnt *= 2
        return arr[:n+1]

        