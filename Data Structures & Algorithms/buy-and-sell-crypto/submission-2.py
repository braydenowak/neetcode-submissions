class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        
        for n in prices:
            if n < minPrice:
                minPrice = n
            elif n - minPrice > profit:
                profit = n - minPrice
                
        return profit

            