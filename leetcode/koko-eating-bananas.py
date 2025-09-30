class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # initialize left and right pointers
        l, r = 1, max(piles)
        # result is r because that is the worst possible solution
        res = r

        # loop through the list until left is less than right
        while l <= r:
            # k is the middle point
            k = (l + r) // 2

            # initialize hours to zero because every loop we have check hours used 
            # and it should go back to 0 so we have calculation for every k
            hours = 0
            # loop through piles and calculate total number of hours with k bananas per hour
            for p in piles:
                hours += math.ceil(p / k)
                
            # check if hours is less or equal than h. If yes, set result to minimum 
            # of res or k. We also need to find less value than this as we need minimum 
            # so we decrease right pointer to find a lesser value
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
            # if hours is greater, we need to increase left pointer as we need to increase 
            # more bananas per hours
                l = k + 1   
    
        return res