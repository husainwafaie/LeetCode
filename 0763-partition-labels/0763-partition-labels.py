class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []
        indexes = {}
        for i in range(len(s)):
            indexes[s[i]] = i
        
        target = indexes[s[0]]
        start = 0
        lst = []
        for i in range(len(s)):
            if i == target:
                lst.append(target - start + 1)
                start = i + 1
                if i != len(s) - 1:
                    target = indexes[s[i+1]]
            else:
                if indexes[s[i]] > target:
                    target = indexes[s[i]]
        if sum(lst) != len(s):
            lst.append(len(s) - sum(lst))
        return lst