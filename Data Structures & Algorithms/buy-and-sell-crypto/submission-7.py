class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
    #     total = 0
    #    # Brute Force Solution
    #     for buy in range(len(prices)):
    #         for sell in range(buy + 1,len(prices)):
    #             profit = prices[sell] - prices[buy]
    #             if profit >= total:
    #                 total = max(profit,total)
            
    #     return total

    # Two Pointer
        left = 0
        right = 1

        total = 0
        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                total = max(profit,total)
            else:
                left = right

            right += 1
        
        return total



