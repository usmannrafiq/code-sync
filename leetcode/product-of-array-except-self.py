class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Time: O(n)
        # Space: O(1) if output array is not considered
        # create an array with number of nums elements
        res = [1] * len(nums)

        # calculate prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # calculate postfix and in the meantime update res with prefix x postfix which
        # will give the product of everything but that element
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        # return the result
        return res