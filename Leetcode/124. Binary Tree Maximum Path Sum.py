# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution :
	"""
	A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
	A node can only appear in the sequence at most once.
	Note that the path does not need to pass through the root.

	where each pair of adjacent nodes in the sequence has an edge connecting them
	: path를 구성하는 각각의 노드들은 각각을 직접 연결하는 edge가 존재한다.
	"""

	def maxPathSum(self, root: Optional[TreeNode]) -> int :
		inf = float("inf")
		mxx = -inf

		def rec(cur) :
			nonlocal mxx
			if cur == None :
				return 0
			now = cur.val
			left = rec(cur.left)
			right = rec(cur.right)
			mxx = max(mxx, now+left+right, left+now, right+now, now)

			return max(now+right, now, now+left)

		rec(root)
		return mxx
