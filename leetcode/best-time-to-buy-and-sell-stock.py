class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # initialize two pointers and max profit
        l, r = 0, 1
        maxprof = 0

        # loop until list is exhausted
        while r < len(prices):
            # compare if right pointer has price greater than left pointer
            if prices[r] > prices[l]:
                # calculate the profit
                profit = prices[r] - prices[l]
                # assign greater value to the max profit to update the profit value
                maxprof = max(maxprof, profit)

            else:
                # if right is not greater than left we assign left new value
                l  = r
            
            # update the right pointer if r is not greater than l 
            r += 1
            
        
        return maxprof