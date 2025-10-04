# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Time: O(n)
        # Space: O(1)
        
        # dummy node to return at the end head of the list
        dummy = ListNode(0, head)
        # left need to be 1 node before n to connect it with the node after n
        left = dummy
        # right starts from head
        right = head

        # to move right n times
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move both pointers
        while right:
            left = left.next
            right = right.next
        
        # connect before n and after n node
        left.next = left.next.next

        # return dummy's next which is the head of the list
        return dummy.next