class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(nums) - 1
            while (l < r):
                n = nums[l] + nums[i] + nums[r]
                if n == 0:
                    ret.add((nums[l], nums[i], nums[r]))
                    l += 1
                    r -= 1
                elif n > 0:
                    r -= 1
                elif n < 0:
                    l += 1
        return ret
        