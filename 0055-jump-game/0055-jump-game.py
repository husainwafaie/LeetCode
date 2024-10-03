class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = nums[0]
        for i in range(len(nums)):
            if index == 0:
                if i == len(nums) - 1:
                    return True
                if nums[i] == 0:
                    return False
                index = nums[i] - 1
            elif nums[i] > index:
                index = nums[i] - 1
            else:
                index -= 1
        return True
