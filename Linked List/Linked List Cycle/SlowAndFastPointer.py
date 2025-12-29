# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty, it cannot have a cycle
        if head is not None:

            # 'small' is the slow pointer (moves 1 step at a time)
            small = head

            # 'large' is the fast pointer (moves 2 steps at a time)
            # Initialized to head.next to avoid immediate equality at start
            large = head.next

            # Continue traversal while both pointers are valid
            while small and large:

                # If slow and fast pointers meet, a cycle exists
                if small == large:
                    return True

                # If either pointer cannot move forward, no cycle is possible
                if not small.next or not large.next:
                    return False

                # Move slow pointer by one step
                small = small.next

                # Move fast pointer by two steps
                large = large.next.next

        # If traversal ends without pointers meeting, no cycle exists
        return False
