class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = 0
        unrobbed = 0
        for i in nums:
            temp = max(unrobbed + i, robbed)
            unrobbed = robbed
            robbed = temp
        return max(robbed, unrobbed)