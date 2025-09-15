class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        # we can use prefix sum for this problem
        # initialize the prefix array
        prefixsum = [nums[0]]

        # iterate through list and update prefix sum
        for i in range(1, len(nums)):
            prefixsum.append(nums[i] + prefixsum[-1])

        # find the minimum prefix sum value (why because if it is less than 1 we can add the 
        # same amount to it and add one to keep it's minimum more than 1)
        minvalue = min(prefixsum)

        # if that value is less than 0, make that value positive and add one so that it never 
        # gets less than 1
        if minvalue < 0:
            return (minvalue * - 1) + 1
        else:
        # if the value is greater than 1, then 1 is the minimum start value we can use because
        # we know it will not go lower than 1
            return 1