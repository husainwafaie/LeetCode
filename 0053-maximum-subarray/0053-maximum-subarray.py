class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        count = float("-inf")
        for i in range(len(nums)):
            if nums[i] > count + nums[i]:
                count = nums[i]
            else:
                count += nums[i]
            if count > maxi:
                maxi = count
        return maxi