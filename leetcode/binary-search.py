class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Time: O(logn): Binary search halves search every iteration
        # Space: O(1): No extra space is being used except constant space by new variables 
        
        # initialize two pointers left and right
        l, r = 0, len(nums) - 1

        # iterate through the loop until left is greater than right
        while l <= r:
            
            # find the midpoint of the list 
            midpoint = r + l // 2

            # if target is greater than the midpoint, set the left greater than half
            if target > nums[midpoint]:
                l = midpoint + 1
             
            # if target is smaller than the midpoint, set the right less than half
            elif target < nums[midpoint]:
                r = midpoint - 1
            
            # loop will iterate until midpoint will be equal to target so return midpoint
            # The last iteration will be when left, right and midpoint are equal and in
            # the next iteration the loop breaks
            else:
                return midpoint
        
        # if there is no target value in the loop
        return -1