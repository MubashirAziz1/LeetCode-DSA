class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j] == 0 or prices[j] <= prices[i]:
                i , j = j , j+1
            else:
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
                j += 1

        return profit
