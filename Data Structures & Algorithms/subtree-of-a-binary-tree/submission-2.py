# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right
        
        q = deque([root])
        while q:
            total = len(q)
            for _ in range(total):
                node = q.popleft()
                if node.val == subRoot.val and isSameTree(node, subRoot):
                    return True
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        
        
        

