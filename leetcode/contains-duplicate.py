class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set which will act as a bucket to store list items
        hashset = set()
        # loop over list items 
        for n in nums:
            # compare list items to hashset and see if there is a duplicate. Remember, the first iteration set is empty
            if n in hashset:
                return True
            # if item is not in hashset, add it to the set. This will ensure that the item is added once and then all the next
            # iterations, that item can be compared to other list items to make sure there are no duplicates.
            hashset.add(n)
        # if there are no duplicates in the list return False
        return False