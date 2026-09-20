class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_diff = 0
        while(r < len(prices)):
            if (prices[l] >prices [r]):
                l = r
            else:
                if(max_diff < prices [r] - prices[l]):
                    max_diff =  prices [r] - prices[l]
            r = r + 1
                
        return max_diff