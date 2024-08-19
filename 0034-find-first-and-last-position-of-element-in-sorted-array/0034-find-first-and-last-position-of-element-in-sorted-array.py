class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = 0
        last = len(nums) - 1
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            return [-1,-1]
        if nums[first] == target:
            last = first
            while last > -1 and last < len(nums) and nums[last] == target:
                last += 1
            return [first, last - 1]
        elif nums[last] == target:
            first = last
            while first > -1 and first < len(nums) and nums[first] == target:
                first -= 1
            return [first + 1, last]
        while last > first + 1:
            mid = int(((last - first) / 2) + first)
            if nums[mid] == target:
                first = mid
                last = mid
                while nums[first] == target:
                    first -= 1
                while nums[last] == target:
                    last += 1
                return [first + 1, last - 1]
            elif nums[mid] > target:
                last = mid
            elif nums[mid] < target:
                first = mid
        return [-1,-1]
        