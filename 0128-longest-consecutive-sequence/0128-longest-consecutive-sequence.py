class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = {}
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        for i in nums:
            if i in dct and i - 1 in dct and dct[i-1] > dct[i] - 1:
                dct[i] = dct[i-1] + 1
            elif i-1 in dct:
                dct[i] = dct[i-1] + 1
            else:
                dct[i] = 1
        return max(dct.values())