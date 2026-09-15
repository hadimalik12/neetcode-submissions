class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        adjlist = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adjlist[i].append(j)
        
        output = []
        vis = set()
        cyc = set()

        def dfs(course):
            if course in cyc:
                return False
            if course in vis:
                return True
                            
            cyc.add(course)
            for i in adjlist[course]:
                if dfs(i) == False:
                    return False
                
            vis.add(course)
            cyc.remove(course)
            output.append(course)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output