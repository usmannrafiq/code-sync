# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Time: O(n)
        # Space: O(1)
        # Tortoise and Hare algorithm
        # we will initialize fast and slow pointers
        slow, fast = head, head

        # make sure that fast can jump two nodes. 
        # if fast is not none and fast.next is not none, it makes sure that 
        # None.next doesnot occur which will cause runtime error
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast is equal to slow, it means that two pointers have caught up
            # and there is a cycle
            if fast == slow:
                return True
            
        # if while loop breaks, it means that there is no cycle as fast pointer has 
        # already pointed to null
        return False