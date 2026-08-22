class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init minBuy as first and maxP = 0 
        # loop through each price with sell
        # update minbuy if smaller is found
        maxP = 0
        minBuy = prices[0]
        
        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP   
