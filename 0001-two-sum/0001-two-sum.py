class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dct and dct[target - nums[i]] != i:
                return [i, dct[target - nums[i]]]