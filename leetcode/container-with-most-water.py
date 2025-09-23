class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Time: O(n)
        # Space: O(1)

        # initialize variables
        res = 0
        l, r = 0, len(height) - 1

        # move through list and store max area in res
        while l < r: 
            area = (r - l) * min(height[r], height[l])
            res = max(area, res)

            # move pointers. If r < l or r = l, move right.
            # In case of equal does not matter which to move.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res