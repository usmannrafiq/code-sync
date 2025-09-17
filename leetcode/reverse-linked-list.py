# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)

        # set previous node to none
        prev = None
        # current is set for the head node 
        curr = head
        # loop through the nodes until curr is None which means list if exhausted
        while curr:
            # save reference to next element from current in a new variable
            next_temp = curr.next
            # move current's next pointer to previous node
            curr.next = prev
            # change previous node to current node
            prev = curr
            # change current node to next node
            curr = next_temp
        # return last node which is the head node for the new list
        return prev