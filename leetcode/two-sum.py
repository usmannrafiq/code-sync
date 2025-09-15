class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to create a hashmap
        hashmap = {}

        # Bind hashmap keys with values while iterating through the list
        # keys = actual value
        # value = index
        # because we need to get the index if we find the complement so we set that as the value
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        # iterate through the list and see if there is a complement in the list and if there
        # is we can get it's value (index) and return it alondside the index of current for
        # iteration (i)

        for i in range(len(nums)):
            complement = target - nums[i]
            # second part of condition is to exclude an edge case like [3,3] with target 6
            # as we don't want to return [0,0]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
        return []