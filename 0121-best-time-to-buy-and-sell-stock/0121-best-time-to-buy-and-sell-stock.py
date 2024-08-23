class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        mini = float("inf")
        for i in prices:
            if i < mini:
                mini = i
            elif i - mini > highest:
                highest = i - mini
        return highest