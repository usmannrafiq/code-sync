# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

    # Time: O(n)
    # Space: O(1)    

    # find the middle
        # slow if first node and fast is the next one
        slow, fast = head, head.next
        # loop until list ends. Move slow one and fast two
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
    # reverse second half
        # pointer for travel through list    
        second = slow.next
        # pointer to point to head
        prev = None
        # slow is the last node of final list so point it to None
        slow.next = None

        while second:
            # we will be breaking second.next so store it in temp first
            temp = second.next
            # reverse the reference 
            second.next = prev
            # prev will point to the second which at the very end will be the head of 
            # reversed list
            prev = second
            # move second pointer to next node (this is where we need temp to travel through list)
            second = temp
        
    # merge with first half

        first, second = head, prev # prev is the head of last half
        while second:
            # we will be breaking these two links so store temps
            temp1, temp2 = first.next, second.next
            # insert head of the reversed second list (prev)
            first.next = second
            # second is inserted between first and temp1
            second.next = temp1
            # update pointers and move forward
            first, second = temp1, temp2