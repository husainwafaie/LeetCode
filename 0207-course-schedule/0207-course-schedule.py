class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        need = {}
        has = {}
        queue = deque()
        for x, y in prerequisites:
            if x not in need:
                need[x] = 0
            if y not in need:
                need[y] = 0
            if x not in has:
                has[x] = set()
            if y not in has:
                has[y] = set()
            need[x] += 1
            has[y].add(x)

        for i in need.keys():
            if need[i] == 0:
                queue.append(i)
        count = 0
        while len(queue) > 0:
            numCourses -= 1
            key = queue.popleft()
            count +=1
            for i in has[key]:
                need[i] -= 1
                if need[i] == 0:
                    queue.append(i)

            if numCourses == 0:
                return True

        if count == len(has.keys()):
            return True
        return False
        
        