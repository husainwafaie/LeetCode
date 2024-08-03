class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        cur_min = float("inf")
        for i in range(len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            elif prices[i] - cur_min > highest:
                highest = prices[i] - cur_min
        return highest