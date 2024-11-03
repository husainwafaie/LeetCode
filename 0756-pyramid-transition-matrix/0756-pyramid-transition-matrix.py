class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        queue = deque()
        dct = {}
        for word in allowed:
            if word[:2] in dct:
                dct[word[:2]].add(word[2])
            else:
                dct[word[:2]] = set([word[2]])
        queue = deque(list(bottom))
        def dfs(q, curr, next):
            out = None
            if curr == next:
                out = q.popleft()
                curr = 0
                next -= 1
            if len(q) == 1:
                return True
            w1 = q.popleft() + q.popleft()
            if w1 not in dct:
                return False
            curr += 1
            q.appendleft(w1[1])
            for word in dct[w1]:
                q.append(word)
                if dfs(q.copy(), curr, next):
                    return True
                q.pop()
            if not out:
                q.appendleft(out)
            return False

        return dfs(queue.copy(), 0, len(queue) - 1)