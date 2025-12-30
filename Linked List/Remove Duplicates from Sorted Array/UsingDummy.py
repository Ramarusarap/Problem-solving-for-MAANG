# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        - The linked list is traversed exactly once.

        Space Complexity: O(1)
        - The list is modified in place using constant extra space.
        """

        # Edge case: empty list or single node list
        if not head or head.next is None:
            return head

        dummy = head     # Points to the last unique node
        temp = head      # Stores the head of the modified list

        # Traverse the list
        while head:
            # Skip nodes with duplicate values
            if head.val == dummy.val:
                head = head.next
            else:
                # Link the last unique node to the next unique value
                dummy.next = head
                dummy = dummy.next

        # Terminate the list to remove leftover duplicate references
        dummy.next = None

        return temp
