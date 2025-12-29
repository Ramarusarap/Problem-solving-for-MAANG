# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted singly linked lists into one sorted list.

        Approach:
        - Use a dummy node to simplify edge cases.
        - Maintain a tail pointer to track the end of the merged list.
        - Compare nodes from both lists and attach the smaller one.
        - Append the remaining nodes once one list is exhausted.

        Time Complexity: O(n + m)
            where n and m are the lengths of the two lists.

        Space Complexity: O(1)
            No extra space used; merging is done in-place.
        """

        dummy = ListNode(-1)
        tail = dummy

        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next  # Advance tail to the newly added node

        # Attach the remaining nodes (only one list can be non-empty)
        tail.next = list1 if list1 else list2

        return dummy.next
