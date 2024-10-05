class Solution:
    def minWindow(self, t: str, s: str) -> str:
        def check(d):
            for i in d.keys():
                if d[i] > 0:
                    return False
            return True
        final = ""
        dct = {}
        for i in s:
            dct[i] = 1 + dct.get(i, 0)
        shortest = float("inf")
        queue = deque()
        for r in range(len(t)):
            if t[r] in dct:
                if queue and t[queue[0]] == t[r] and dct[t[r]] <= 0:
                    queue.popleft()
                    queue.append(r)
                else:
                    queue.append(r)
                    dct[t[r]] -= 1
                if check(dct):
                    if queue[-1] - queue[0] + 1 < shortest:
                        shortest = queue[-1] - queue[0] + 1
                        final = t[queue[0]:queue[-1] + 1]
                    num = queue.popleft()
                    dct[t[num]] += 1
                    while check(dct):
                        if queue[-1] - queue[0] + 1 < shortest:
                            shortest = queue[-1] - queue[0] + 1
                            final = t[queue[0]:queue[-1] + 1]
                        num = queue.popleft()
                        dct[t[num]] += 1
        return final