class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initializing k to zero which is the count for number of different values
        k = 0
        # loop through the list
        for i in range(len(nums)):
            # if value is not equal to required value, we swap k index with i index value
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # return k value
        return k