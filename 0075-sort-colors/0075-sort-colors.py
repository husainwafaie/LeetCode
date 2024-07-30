class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        for i in range(index, len(nums)):
            if nums[i] == 1:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        