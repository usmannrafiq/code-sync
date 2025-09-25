class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Time: O(n2) as n2 is the longer one else false is returned
        # Space: O(1)

        # initialize length variables
        n1 = len(s1)
        n2 = len(s2)

        # if n1 is greater there is no possibility of permutation
        if n1 > n2:
            return False
        
        # initialize arrays to store 26 characters a - z
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        # first we check length of n1 characters in both
        for i in range(n1):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        # if there is a permutation no need to solve further
        if count_s1 == count_s2:
            return True
        
        # if n1 length in n2 does not contain permutation, 
        # we carry on with the n2 further starting from where n1 length ended
        for i in range(n1, n2):
            # add one value
            count_s2[ord(s2[i]) - ord('a')] += 1
            # subtract one value
            count_s2[ord(s2[i - n1]) - ord('a')] -= 1
            # everytime one value is added or subtracted we check with
            # permutation possibility
            if count_s1 == count_s2:
                return True
        
        return False