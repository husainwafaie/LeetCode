class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst = []

        def helper(rem, l, start):
            if rem < 0:
                return
            elif rem == 0:
                lst.append(l.copy())
                return
            for i in range(start, len(nums)):
                l.append(nums[i])
                helper(rem - nums[i], l, i)
                l.pop()
        for i in range(len(nums)):
            helper(target - nums[i], [nums[i]], i)
        return lst