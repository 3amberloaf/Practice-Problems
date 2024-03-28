#You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by 
# choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    @staticmethod
    def maxProfit(prices):
        
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit


# Example usage
prices = [7, 1, 5, 3, 6, 4]
result = Solution.maxProfit(prices)
print(result)

