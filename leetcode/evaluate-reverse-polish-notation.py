class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time: O(1)
        # Space: O(n)
        stack = []

        # go through each element in stack and do operations on two values
        # that were added before the current one
        for c in tokens:
            # there are only 4 conditions here: +, *, /, - else it's an integer we add
            # to the stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            else:
                stack.append(int(c))
        # return the only value that is left in the stack
        return stack[0]