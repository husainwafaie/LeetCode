class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        l, r = 0, len(nums)
        while l < r:
            mid = int((r + l) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target and nums[mid - 1] < target:
                return mid
            if nums[mid] < target and nums[mid + 1] > target:
                return mid + 1
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid
            
        return -1
        