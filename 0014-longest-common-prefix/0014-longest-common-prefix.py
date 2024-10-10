class Solution:
    def longestCommonPrefix(self, nums: List[str]) -> str:
        prefix = nums[0]
        for i in range(1, len(nums)):
            p = 0
            while p < len(nums[i]) and p < len(prefix) and prefix[p] == nums[i][p]:
                p += 1
            prefix = prefix[:p]
        return prefix