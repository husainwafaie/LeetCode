class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp = 0
        l,r = 0, len(height) - 1
        while l != r:
            if min(height[l], height[r]) * (r - l) > temp:
                temp = min(height[l], height[r]) * (r - l)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return temp
