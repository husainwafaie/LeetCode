class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        used = [0] * len(nums)

        def helper(l, used):
            if len(l) == len(nums):
                lst.append(l.copy())
                return
            for i in range(len(nums)):
                if used[i] == 0:
                    used[i] = 1
                    l.append(nums[i])
                    helper(l, used)
                    l.pop()
                    used[i] = 0
        helper([], used)
        return lst