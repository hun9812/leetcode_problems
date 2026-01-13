class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        exp = 0
        if num1 == "0" or num2 == "0":
            return "0"
        res = ""
        for i in num2[::-1]:
            cur = ""
            for _ in range(int(i)):
                cur = self.addStrings(cur, num1)
            for _ in range(exp):
                cur += "0"
            exp += 1
            # print(cur)
            res = self.addStrings(res, cur)
        
        return res

    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0  # 올림수
        
        # 두 숫자의 마지막 인덱스부터 시작
        i = len(num1) - 1
        j = len(num2) - 1
        
        # 두 문자열 중 하나라도 남았거나 올림수가 있는 동안 반복
        while i >= 0 or j >= 0 or carry:
            # 각 자리의 숫자 추출 (인덱스가 끝나면 0으로 처리)
            # ord('0')은 48이므로, ord(char) - 48을 하면 실제 정수값이 나옵니다.
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # 합계 계산
            total = n1 + n2 + carry
            carry = total // 10    # 다음 자리로 넘길 올림수
            digit = total % 10     # 현재 자리에 남을 숫자
            
            res.append(str(digit)) # 현재 숫자를 결과 리스트에 추가
            
            # 인덱스 앞으로 이동
            i -= 1
            j -= 1
        
        # 리스트를 뒤집어서 문자열로 합치기
        return "".join(res[::-1])
            