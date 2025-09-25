# Question : 
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Answer

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

def binary_tree(arr):

    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

sol = Solution()
arr = [1,None,2,3]
root = binary_tree(arr)
res = sol.inorderTraversal(root)
print(res)