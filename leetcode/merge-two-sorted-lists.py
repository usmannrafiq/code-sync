# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        # Time: O(n)
        # Space: O(1)
        
        # initialize a dummy node to keep track of start
        # if there is no dummy node, we'll need to compare list1 and list 2
        # to get the head node.

        dummy = ListNode()
        # this is the tail node which we'll use to add values after comparing
        tail = dummy

        # loop condition to go through lists and compare nodes until one of the lists is empty
        while list1 and list2:
            # if list1 node is less
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # if list2 node is equal or less
            else:
                tail.next = list2
                list2 = list2.next
            # we always move tail node to the next in both cases
            tail = tail.next
        
        # to check if any of the list has remaining nodes
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        # return the head node which is the next node than the dummy node.
        return dummy.next