class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        chosen = [0] * len(candidates)
        lst = []
        def dfs(index, l, chosen):
            if sum(l) == target:
                lst.append(l.copy())
                return
            if sum(l) > target:
                return
            for i in range(index, len(candidates)):
                if i and candidates[i] == candidates[i-1] and chosen[i-1] == 0:
                    continue
                l.append(candidates[i])
                chosen[i] = 1
                dfs(i+1, l, chosen)
                chosen[i] = 0
                l.pop()

        for i in range(len(candidates)):
            if i and candidates[i] == candidates[i-1]:
                continue
            chosen[i] = 1
            dfs(i+1, [candidates[i]], chosen)
            chosen[i] = 0
        return lst