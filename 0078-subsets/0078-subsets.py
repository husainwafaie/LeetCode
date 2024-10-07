class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [[]]
        def helper(n, s):
            lst.append(n.copy())
            for i in range(s+1, len(nums)):
                n.append(nums[i])
                helper(n, i)
                n.pop()

        for i in range(len(nums)):
            helper([nums[i]], i)
        return lst