class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Time: O(n^2)
        # Space: O(1) or O(m) for output array

        # initialize output array and sort the output
        res = []
        nums.sort()

        # we put anchor with a and then utilize two sum for the other two values to find the total
        # sum of 0. (enumerate gets value and the index)
        for i, a in enumerate(nums):
            # check if we are not on the first value and the next value is not the same as before
            # if it is same means that triplet is gonna be same so we skip it
            if i > 0 and a == nums[i - 1]:
                continue
            # initialize two pointers and find possible triplets that sum to 0
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                
                elif threesum > 0:
                    r -= 1
                # we found triplet and we store it in result array
                else:
                    res.append([a, nums[l], nums[r]])
                    # move pointers
                    l += 1
                    r -= 1
                    # We move left pointer until unique value comes. We do this to avoid same triplet duplication
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res