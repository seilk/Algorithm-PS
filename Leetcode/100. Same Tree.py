# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution :

	def compare(self, root1, root2) :
		if root1 == None :
			if root2 == None :
				return True
			else :
				return False
		if root2 == None :
			if root1 == None :
				return True
			else :
				return False

		if root1.val != root2.val :
			return False
		if self.compare(root1.right, root2.right) == False :
			return False
		if self.compare(root1.left, root2.left) == False :
			return False

		return True

	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool :
		ans = self.compare(p, q)
		return ans
