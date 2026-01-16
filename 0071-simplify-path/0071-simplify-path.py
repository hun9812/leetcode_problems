class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path_list = list(path.split("/"))

        for i in path_list:
            if i == "":
                continue
            elif i == "..":
                if res:
                    res.pop()
            elif i == ".":
                continue
            else:
                res.append(i)

        res_str = ""
        for i in res:
            res_str += "/" + i
        
        if len(res_str) == 0:
            return "/"
        else:
            return res_str