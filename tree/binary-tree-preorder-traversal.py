# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    # recursive helper function
    def preorder(self, root):
        # base case
        if root is None:
            return

        # Root
        self.ans.append(root.val)

        # Left
        self.preorder(root.left)

        # Right
        self.preorder(root.right)

    # main function called by judge
    def preorderTraversal(self, root):
        self.ans = []              # reset list
        self.preorder(root)        # start recursion
        return self.ans

#class Solution:
    #def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        