class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst = []
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

        def helper(l):
            if len(l) == len(nums):
                lst.append(l.copy())
                return
            for i in dct.keys():
                if dct[i] > 0:
                    dct[i] -= 1
                    l.append(i)
                    helper(l)
                    l.pop()
                    dct[i] += 1

        helper([])
        
        return lst
            