class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)

        # initialize a hashset
        hashSet = set()

        # initialize length and pointer variables
        length = 0
        l, r = 0, 0

        # loop through the string
        for r in range(len(s)):
            # remove duplicates until there are none
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            # add r every iteration after removing duplicates which makes sure
            # we are counting correct length of the substring (no duplicates)
            hashSet.add(s[r])
            length = max(length, r - l + 1)

        return length