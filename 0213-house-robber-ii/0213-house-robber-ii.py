class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def find_max(nums):
            r1,r2= 0,0
            for i in nums:
                if i + r1 > r2:
                    temp = i + r1
                else:
                    temp = r2
                r1 = r2
                r2 = temp
            return max(r1,r2)
        a = find_max(nums[1:])
        b = find_max(nums[:-1])
        if a > b:
            return a
        return b
