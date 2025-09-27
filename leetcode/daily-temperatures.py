class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # initialize variables
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stk = [] # pair: [temp, index]

        # get index and temperatures
        for i, t in enumerate(temps):
            # while stack is not empty and top most stack value is less
            # than temperature in the list
            while stk and stk[-1][0] < t:
                # pop stack index
                stk_t, stk_i = stk.pop()
                # store index in 
                answer[stk_i] = i - stk_i
            # if stack is empty or temp value is greater in stack
            stk.append((t, i))
        return answer