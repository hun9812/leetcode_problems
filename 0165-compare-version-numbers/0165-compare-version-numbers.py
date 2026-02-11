class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = list(version1.split("."))
        v2_list = list(version2.split("."))
        
        for i in range(min(len(v1_list), len(v2_list))):
            cur_v1 = v1_list[i]
            cur_v2 = v2_list[i]
            while cur_v1 != "":
                if cur_v1[0] == "0":
                    cur_v1 = cur_v1[1:]
                else:
                    break
            while cur_v2 != "":
                if cur_v2[0] == "0":
                    cur_v2 = cur_v2[1:]
                else:
                    break
            if cur_v1 == cur_v2:
                continue
            if cur_v1 == "":
                return -1
            if cur_v2 == "":
                return 1
            if int(cur_v1) > int(cur_v2):
                return 1
            else:
                return -1
        
        if len(v1_list) > len(v2_list):
            for i in range(len(v2_list), len(v1_list)):
                cur_v1 = v1_list[i]
                while cur_v1 != "":
                    if cur_v1[0] == "0":
                        cur_v1 = cur_v1[1:]
                    else:
                        break
                if cur_v1 =="":
                    continue
                else:
                    return 1
        if len(v1_list) < len(v2_list):
            for i in range(len(v1_list), len(v2_list)):
                cur_v2 = v2_list[i]
                while cur_v2 != "":
                    if cur_v2[0] == "0":
                        cur_v2 = cur_v2[1:]
                    else:
                        break
                if cur_v2 =="":
                    continue
                else:
                    return -1
        return 0