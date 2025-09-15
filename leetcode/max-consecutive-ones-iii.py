class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # zeros represent the number of 0s
        zeros = 0
        left = ans = length = 0

        # we need to iterate through the list and move pointers 
        # right will move itself because of for loop
        
        for right in range(len(nums)):
            # if we find 0 at right pointer, we increase zero counter
            if nums[right] == 0:
                zeros += 1
            
            # we check in every for loop iteration that zero have exceeded the limit or not
            # if they have, we use while condition to remove zero until constraint is valid again

            while zeros > k:
                if nums[left] == 0:
                # we decrease zeros while moving left pointer 
                    zeros -= 1
                left += 1
            
            # formula to calculate length of a valid subarray. Above conditions will make sure
            # we have a valid subarray up this point so we store it's length here.
            length = right - left + 1
            
            # We compare the length of previous maximum with current subarray length and only
            # store if it's greater than previous maximum
            
            ans = max(ans, length)
            
        return ans