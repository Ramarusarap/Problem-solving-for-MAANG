# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

        Approach:
        - Use two pointers:
            slow moves one step at a time
            fast moves two steps at a time
        - If a cycle exists, slow and fast will eventually meet.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
