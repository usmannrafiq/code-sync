class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if length not equal means they are not anagrams
        if len(s) != len(t):
            return False

        # we need to create 2 hashmaps

        countS, countT = {}, {}

        # iterate through the range and add both string counts to the hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # compare the mapping i.e same keys and values
        return countS == countT