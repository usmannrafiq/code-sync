class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initialize a dic/hashmap that stores the count of numbers in the list             
        count = {}
        # initialize a bucket which stores lists and numbers in those lists
        # lists will reside as their index = count of elements inside that list
        # freq = [[], [], [], [], [], []]
        freq = [[] for i in range(len(nums) + 1)]

        # we need to put values in hashmap
        # num as key and count as values
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # transfer values from hashmap to the bucket
        for n, c in count.items():
            freq[c].append(n)
        
        # initiate our result list that we will return
        res = []
        # loop through freq list and return nums with k frequency occurance
        # start from the end 
        for i in range(len(freq) - 1, 0, -1):
            # get nums from list within freq list: [[]]
            for num in freq[i]:
                # add num to the result list
                res.append(num)
                # check if k elements are there
                if len(res) == k:
                    return res