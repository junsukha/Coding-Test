
# Python 3 program for the above approach
 
 
# Function to find maximum profit possible
# by buying and selling at most one stack
def findMaximumProfit(prices, i,  k,
                      buy, v):
 
    # If no stock can be chosen
    if (i >= len(prices) or k <= 0):
        return 0
 
    if (v[i][buy] != -1):
        return v[i][buy]
 
    # If a stock is already bought
    if (buy):
        v[i][buy] = max(-prices[i]
                        + findMaximumProfit(prices, i + 1, k, not buy, v),
                        findMaximumProfit(prices, i + 1, k, buy, v))
        return v[i][buy]
 
    # Otherwise
    else:
        # Buy now
        v[i][buy] = max(prices[i] + findMaximumProfit(prices, i + 1, k - 1, not buy, v),
            findMaximumProfit(prices, i + 1, k, buy, v))
        return v[i][buy]
 
 
# Function to find the maximum
# profit in the buy and sell stock
def maxProfit(prices):
 
    n = len(prices)
    v = [[-1 for x in range(2)]for y in range(n)]
 
    # buy = 1 because atmost one
    # transaction is allowed
    return findMaximumProfit(prices, 0, 1, 1, v)

class Solution:
    def maxProfit(self, prices):
        
        n = len(prices)
        if n < 2:
            return 0
        maxprofit, minstock = float('-inf'), prices[0]
        for p in prices:
            maxprofit = max(maxprofit, p-minstock)
            minstock = min(minstock, p)
        return maxprofit
    
solution = Solution()
sol = solution.maxProfit([5,1,2,3])
print(sol)


class MySolution:
    def findMaxProfit(self, prices):
        maxprofit = float('-inf')
        minstock = prices[0]
        for price in prices:
            maxprofit = max(maxprofit, price - minstock)
            minstock = min(price, minstock)
        
        return maxprofit

solution = MySolution()
sol = solution.findMaxProfit([4,6,2,3])
print(sol)