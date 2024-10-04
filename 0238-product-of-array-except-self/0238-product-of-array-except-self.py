import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        running = 1
        for i in range(len(nums)):
            running *= nums[i]
            left.append(running)
        
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            running *= nums[i]
            right.append(running)
        right.reverse()
        
        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append(right[1])
            elif i == len(nums) - 1:
                ret.append(left[-2])
            else:
                ret.append(left[i - 1] * right[i + 1])
        return ret
