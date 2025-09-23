class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Time: O(n)
        # Space: O(n)
        
        # initialize a hashset for comparisons
        numSet = set(nums)
        # streak is the longest sequence
        # length is to track current streak while in the loop
        streak = 0
        
        # Traverse through the list and compare to the hashset
        for n in numSet:
            # check if it's start of the sequence or not. If its not:
            if (n - 1) not in numSet:
                # as the sequence starts now, length should be set to 1 because it 
                # is a new sequence.
                length = 1
                # loop until next sequence value is not in the hashset
                while (n + length) in numSet:
                    length += 1
                # update the streak
                streak = max(length, streak)
            
        return streak