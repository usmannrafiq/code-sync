"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Time: O(n)
        # Space: O(n)

        # create a hashmap to store original node as keys and copies as values. Include None for edge case 
        oldToCopy = {None: None}

        # loop through nodes and make a deep copy without linking
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        # link nodes to next and random as in the original
        curr = head
        while curr:
            # fetch copy node from hashmap stored as value of original node (key/curr)
            copy = oldToCopy[curr]
            # copy.next will link as the original is linked curr.next
            copy.next = oldToCopy[curr.next]
            # copy.random will link as the original is linked curr.random
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]