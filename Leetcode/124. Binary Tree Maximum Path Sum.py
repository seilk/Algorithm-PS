# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution :

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