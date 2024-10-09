class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dct = {}
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            if i > 0:
                nums[i] += nums[i-1]
            if nums[i] not in dct:
                dct[nums[i]] = i
            if nums[i] == 0:
                if i + 1 > longest:
                    longest = i + 1
            elif dct[nums[i]] != i:
                if i - dct[nums[i]] > longest:
                    longest = i - dct[nums[i]]
        return longest
        
