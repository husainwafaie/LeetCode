class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running = 0
        highest = float("-inf")
        for i in range(len(nums)):
            running += nums[i]
            if running > highest:
                highest = running
            if running < 0:
                running = 0
        return highest