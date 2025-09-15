class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
        # we can assign left and right (swap places in a single line)
            s[left], s[right] = s[right], s[left]
            # decrement both variables in a single line as well
            left, right = left + 1, right - 1