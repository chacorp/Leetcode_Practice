# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        a=[]
        if root==None:
            return
        tn_l=self.inorderTraversal(root.left)
        tn_r=self.inorderTraversal(root.right)
        
        if tn_l is not None:
            for l in tn_l:
                a.append(l)
                
        a.append(root.val)
        
        if tn_r is not None:
            for r in tn_r:
                a.append(r)       

        return a
