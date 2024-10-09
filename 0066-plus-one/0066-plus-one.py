class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        while p > -1:
            if digits[p] < 9:
                digits[p] += 1
                return digits
            else:
                digits[p] = 0
                p -= 1
        digits.insert(0, 1)
        return digits