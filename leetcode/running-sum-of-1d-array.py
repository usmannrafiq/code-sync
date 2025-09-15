class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # create an array to store prefix sum and set first element of array to first
        # element of list as that is the first prefix sum
        prefix = [nums[0]]
        
        # loop through the list by starting from 1 as 0 is already accounted for
        # sum i element from nums list to the latest element in prefix array to find
        # the current sum and add it to the array
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        # return the prefix array
        return prefix