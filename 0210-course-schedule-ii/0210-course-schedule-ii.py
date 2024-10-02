class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need = {}
        has = {}
        queue = deque()
        steps = []
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

        for i in range(numCourses):
            if i not in need:
                steps.append(i)
            elif need[i] == 0:
                queue.append(i)
        count = 0
        while len(queue) > 0:
            numCourses -= 1
            key = queue.popleft()
            steps.append(key)
            count +=1
            for i in has[key]:
                need[i] -= 1
                if need[i] == 0:
                    queue.append(i)

            if numCourses == 0:
                return steps

        if count == len(has.keys()):
            return steps
        return []