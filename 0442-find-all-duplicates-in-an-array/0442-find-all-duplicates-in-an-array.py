class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index - 1] < 0:
                ret.append(index)
            else:
                nums[index - 1] = -1 * nums[index - 1]

        return ret