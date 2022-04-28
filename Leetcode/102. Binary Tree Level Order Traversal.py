# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from typing import Optional, List

class Solution :

	def dfs(self, depth, cur) :
		global dix
		if cur == None :
			return
		dix[depth].append(cur.val)
		self.dfs(depth+1, cur.left)
		self.dfs(depth+1, cur.right)

	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]] :
		global dix
		dix = defaultdict(list)
		self.dfs(0, root)

		return list(dix.values())
