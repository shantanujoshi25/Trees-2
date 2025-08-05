# // Time Complexity : O(n)
# // Space Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        self.idx = len(inorder)
        self.map = {val : idx for idx,val in enumerate(inorder)}


        def helper(left,right):
            
            if(left > right or self.idx < 0):
                return None

            self.idx-=1
            root = TreeNode(postorder[self.idx])

            inorder_idx = self.map[root.val]
            root.right = helper(inorder_idx+1,right)
            root.left = helper(left,inorder_idx-1)
            
           
            return root


        root = helper(0,len(inorder)-1)
        return(root)


     


        