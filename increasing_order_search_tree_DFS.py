# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        val = []
        self.__inorder(root,val)
        ans  = cur = TreeNode(None)
        
        for x in val:
            cur.right = TreeNode(x)
            cur = cur.right

        return ans.right
    
    def __inorder(self,node,val):
            if node:
                self.__inorder(node.left,val)
                val.append(node.val)
                self.__inorder(node.right,val)

            
        
        
