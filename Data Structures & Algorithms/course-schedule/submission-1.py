class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adjlist[i].append(j)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            
            visit.add(course)
            for neighbor in adjlist[course]:
                if not dfs(neighbor):
                    return False
            visit.remove(course)
            adjlist[course] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        
