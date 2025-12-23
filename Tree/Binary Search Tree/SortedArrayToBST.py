# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Builds a height-balanced Binary Search Tree (BST)
        from a sorted array using divide-and-conquer.
        """

        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct a subtree
            if left > right:
                return None

            # Choose the middle element to ensure balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            # Return the root of the constructed subtree
            return root

        # Build the BST from the full array
        return build(0, len(nums) - 1)


Time Complexity

O(n)
Each element in the array is used exactly once to create a tree node.
No repeated work or nested loops.

Space Complexity
O(log n) (average case)
Due to recursion stack depth in a balanced BST.
In worst case (theoretical), recursion stack could go up to O(n), but this construction guarantees balance.
