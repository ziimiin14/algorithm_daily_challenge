# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                val.append(node.val)
                inorder(node.right)
        
        val = []
        inorder(root)
        ans  = cur = TreeNode(None)
        
        for x in val:
            cur.right = TreeNode(x)
            cur = cur.right

        return ans.right

            
        
        
