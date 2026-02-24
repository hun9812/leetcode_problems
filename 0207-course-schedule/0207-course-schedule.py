class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        visited = set()
        cur_visit = set()
        
        def dfs(node):
            if node in cur_visit:
                return False
            if node in visited:
                return True
            
            cur_visit.add(node)
            for next_course in graph[node]:
                if not dfs(next_course):
                    return False
                    
            cur_visit.remove(node)
            visited.add(node)
            
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True