class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        We need two pointers here. We can go through both strings and see if we get a match. If we don't we can delete
        character from the second string and carry on. If the length of both strings is equal, that means we have a match'
        and first string is a subsequence of the second string.
        
        Time: O(n) Iterate once through whole string worst case
        Space: O(1) No additional storage
        """

        # setting up two pointers
        i = j = 0
        # loop through both strings and if match is found increment i, else increment j.
        while i < len(s) and j < len(t):
            # so if there is a match, we keep track of that character with the help of count and that is stored in i.
            if s[i] == t[j]:
                i += 1
            # if there is a match or not, we have to move pointer on the second string to compare next character.
            j += 1
        # if the length of i is equal to string s, it means we found same no of characters in both strings with sequence.
        # Remember: 
        #   We don't need to know what is the character. We just find the match and increment i
        #   Also, we make sure that characters are in sequence by comparing them side by side which is important else we could also have used 
        #   if in etc
        return i == len(s)