class Solution:
    def isValid(self, s: str) -> bool:

        # we'll be using stack for this problem (LIFO). Stack only stores opening brackets
        stack = []

        # Hashmap to store closing brackets as keys and opening as values. Close to opening to
        # check if stack has opening by comparing opening to opening
        closeToOpen = {")": "(", "}": "{", "]": "["}

        # loop through string
        for i in s:
            # if closing bracket
            if i in closeToOpen:
                # make sure stack is not empty else return false because there was no opening bracket for this
                # we pull out the latest stack value and see if it matches our iteration bracket value. If it does
                # it means it is the closing bracket for that opening one. We remove it from stack as we no longer
                # need it in stack after proving it's existing
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()

                else:
                    # it was a different closing bracket than the opening one in the stack
                    return False
            else:
                # if it's an opeing bracket
                stack.append(i)

        # if stack is empty return True, False otherwise
        return True if not stack else False