# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time: O(n)
        # Space: O(1)

        # dummy node to return head at the end
        dummy = ListNode()
        # start curr from dummy to link curr and dummy together
        curr = dummy

        # carry outside the loop
        # carry is outside the loop because it represents state carried over between iterations — 
        # just like in manual addition, you remember the carry until it’s gone.
        carry = 0

        while l1 or l2 or carry:
            
            # if value is there then assign it or it'll be 0 as rule for addition
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # we need to add both values and possible carry together to get the digit
            val = v1 + v2 + carry
            # division by 10 gives anything after unit
            carry = val // 10
            # modulo gives the remainder which is the last digit (unit)
            val = val % 10
            # assign value to the new node that we will create each iteration
            curr.next = ListNode(val)

            # update pointers. If value is there take it else, None
            # We do this because if not done will search for None.next and that will cause
            # attribute erro 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next