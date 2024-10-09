class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0: 1}
        count = 0
        prev = 0
        for num in nums:
            prev += num
            if prev - k in dct:
                count += dct[prev - k]
            dct[prev] = 1 + dct.get(prev, 0)
        return count
            