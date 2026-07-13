class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
       # Brute Force Solution
        for buy in range(len(prices)):
            for sell in range(buy + 1,len(prices)):
                profit = prices[sell] - prices[buy]
                if profit >= total:
                    total = max(profit,total)
            
        return total