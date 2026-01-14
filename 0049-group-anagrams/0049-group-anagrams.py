class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        group_dict = []
        
        for s in strs:
            if len(s) == 0:
                empty_group = -1
                for u in range(len(group)):
                    if len(group[u][0]) == 0:
                        empty_group = u
                        break
                if empty_group != -1:
                    group[empty_group].append(s)
                else:
                    group.append([""])
                    empty_dict = {}
                    group_dict.append(empty_dict)
                continue


            check = -1
            for i in range(len(group)):
                if len(group[i][0]) != len(s):
                    continue
                if check != -1:
                    break
                check_dict = group_dict[i].copy()
                for j in range(len(s)):
                    if s[j] not in check_dict:
                        break
                    else:
                        check_dict[s[j]] -= 1
                        if check_dict[s[j]] < 0:
                            break
                        if j == len(s)-1:
                            check = i
                if check >= 0:
                    if len(s) == len(group[check][0]):
                        group[check].append(s)
                    else:
                        check = -1

            if check == -1:
                # new gourp
                cur_dict = {}
                for c in s:
                    if c in cur_dict:
                        cur_dict[c] += 1
                    else:
                        cur_dict[c] = 1
                group.append([s])
                group_dict.append(cur_dict)
        return group