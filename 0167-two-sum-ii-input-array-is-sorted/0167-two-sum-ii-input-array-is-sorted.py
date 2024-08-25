class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while r > l:
            num = numbers[l] + numbers[r]
            if num == target:
                return [l+1, r+1]
            elif num > target:
                r -= 1
            else:
                l += 1