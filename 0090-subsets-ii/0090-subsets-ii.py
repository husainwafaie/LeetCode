class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = [[]]
        nums.sort()
        def helper(n, s):
            lst.append(n.copy())
            i = s + 1
            while i != len(nums):
                n.append(nums[i])
                helper(n, i)
                n.pop()
                i += 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    i += 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            helper([nums[i]], i)
        return lst