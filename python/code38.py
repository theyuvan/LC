# Question : 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Answer

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first = float('inf')
        final = 0

        for price in prices:
            if price < first:
                first = price
            elif price - first > final:
                final = price - first

        return final

sol = Solution()
prices = [2, 8, 6, 1]
res = sol.maxProfit(prices)
print(res)