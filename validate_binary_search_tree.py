# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# def isValidBST(root):
#     """
#     :type root: TreeNode
#     :rtype: bool
#     """
#     return isValidBSTHelper(root, sys.maxint, -sys.maxint-1)
    
# def isValidBSTHelper(root, mini, maxi):
#     if root is None:
#         return True
    
#     if root[1] < mini or root[1] > maxi:
#         return False
    
#     return isValidBSTHelper(root[1:], mini, root[0] - 1) and 
# isValidBSTHelper(root[2:], root[0]+1, maxi)
    


# class TreeNode:
#     def __init__(self, data, left = None, right = None):
#         self.data = data
#         self.left = left
#         self.right = right

# def insert(temp, data):
#     que = []
#     que.append(temp)
#     while (len(que)):
#         temp = que[0]
#         que.pop(0)
#         if (not temp.left):
#             if data is not None:
#                 temp.left = TreeNode(data)
#             else:
#                 temp.left = TreeNode(0)
#             break
#         else:
#             que.append(temp.left)
        
#         if (not temp.right):
#             if data is not None:
#                 temp.right = TreeNode(data)
#             else:
#                 temp.right = TreeNode(0)
#             break
#         else:
#             que.append(temp.right)
            
# def make_tree(elements):
#     Tree = TreeNode(elements[0])
#     for element in elements[1:]:
#         insert(Tree, element)
#     return Tree



import sys

# def isValidBST(self, root):
#     return self.solve(root,-sys.maxsize,sys.maxsize)
# def solve(self,root,min_val,max_val):
#     if root == None or root.data == 0:
#         return True
#     if (root.data <= min_val or root.data >=max_val):
#         return False
#     return self.solve(root.left,min_val,root.data) and self.solve(root.right,root.data,max_val)

# MAX_INT = sys.maxsize
# print(MAX_INT)
# # print(sys.intmax)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        max_value = sys.maxsize
        min_value = -sys.maxsize
        return self.solve(root, min_value, max_value)
        
    
        
    def solve(self, root, min_, max_):   
        if root == None:
            return 1
        
        if root.val >= max_ or root.val <= min_:
            return 0
        return self.solve(root.left, min_, root.val) and self.solve(root.right, root.val, max_)