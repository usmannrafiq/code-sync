class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize left and right pointers 
        l, r = 0, len(s) - 1

        # Move pointers until they meet
        while l < r:
            
            # Increase left pointer until we find alphanumeric (skip all other char)
            while l < r and not s[l].isalnum():
                l += 1
            # Decrease right pointer until we find alphanumeric (skip all other char)
            while r > l and not s[r].isalnum():
                r -= 1
            # compare characters in lower case. 
            if s[l].lower() != s[r].lower():
                return False
            # increase the count if the comparison was right this iteration
            l += 1
            r -= 1
        # if all the comparisons were good, return true as it is palindrome
        return True