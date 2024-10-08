class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0
        while r < len(nums) - 1:
            maxi = 0
            for i in range(l, r+1):
                maxi = max(maxi, nums[i] + i)
            l = r + 1
            r = maxi
            count += 1
        return count