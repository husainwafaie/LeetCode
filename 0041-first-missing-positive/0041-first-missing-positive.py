class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        num = 1
        while num in nums:
            num += 1
        return num