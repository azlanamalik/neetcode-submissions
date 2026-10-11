class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index1 = 0
        index2 = 1
        maximum = 0
        while (index2 < len(prices)):
            if prices[index2] < prices[index1]:
                index1 = index2
                index2 += 1
            else:
                maximum = max(maximum , prices[index2] - prices[index1])
                index2 += 1
        return maximum