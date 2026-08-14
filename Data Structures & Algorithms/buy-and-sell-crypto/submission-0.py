class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        res = 0
        while i < len(prices)-1:
            j = i+1
            while j<len(prices):
                curr_max = prices[j]-prices[i]
                res = max(res, curr_max)
                j+=1
            i+=1
        return res
                
        