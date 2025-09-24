class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # initialize hashmap and result variables
        count = {}
        res = 0

        # left pointer is set to 0
        l = 0

        # maxf is the max frequency of a value.
        # It stays at max and we don't decrease it even if the window
        # is shrinked
        maxf = 0

        for r in range(len(s)):
            # add count to the dictionary with count as values
            count[s[r]] = 1 + count.get(s[r], 0)
            # we increase maxf if current count of r is more than previous 
            # frequency
            maxf = max(maxf, count[s[r]])

            # condition determines if number of replacememts is less than or 
            # equal to k. It makes sure that the window length that we record 
            # in res is a valid window
            while (r - l + 1) - maxf > k:
                # while the condition is not fulfilled, we remove values from left
                # and decrease the count as well
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res