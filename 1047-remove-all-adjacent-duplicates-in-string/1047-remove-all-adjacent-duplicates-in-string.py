class Solution:
    def removeDuplicates(self, s: str) -> str:
        did = s[0]
        i = 1
        while i < len(s):
            if len(did) != 0 and did[-1] == s[i]:
                did = did[:-1]
                i += 1
                check = True
                while check:
                    if len(did) == 0 or i >= len(s):
                        break
                    if did[-1] == s[i]:
                        did = did[:-1]
                        i += 1
                    else:
                        check = False
            else:
                did += s[i]
                i += 1
        return did
        