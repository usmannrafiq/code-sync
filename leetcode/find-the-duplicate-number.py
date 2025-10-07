class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # two pointer
        slow, fast = 0, 0
        
        # first interaction
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Another slow pointer
        slow2 = 0

        # second interaction will be the number that is the duplicate
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow