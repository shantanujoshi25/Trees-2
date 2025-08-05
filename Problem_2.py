# // Time Complexity : O(n)
# // Space Complexity : O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumPath(root,TotalSum,num):
            
            num = root.val + num * (10)
            
            if(root.left is None and root.right is None):
                TotalSum += num 
            
            if(root.left):
                TotalSum = sumPath(root.left,TotalSum,num)
            if(root.right):
                TotalSum = sumPath(root.right,TotalSum,num)

            return TotalSum
            
        return sumPath(root,0,0)

        