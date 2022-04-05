from typing import List

class Solution :

	def maxArea(self, height: List[int]) -> int :
		"""
		높이*너비 값을 가장 크게 하기 위해서 양 끝의 막대 중 더 큰 막대를 선택하면서 너비를 1씩 줄여나간다.
		정해진 너비에서 가능한 최대 높이의 막대를 선택한다.
		매 순간 최대 높이의 막대를 고정시키면 정해진 너비에서의 최대 넓이를 구할 수 있다.
		"""
		left = 0
		right = len(height)-1
		ans = 0
		while left < right :
			ans = max(ans, min(height[right], height[left])*(right-left))

			if height[right] < height[left] :
				right -= 1
			else :
				left += 1

		return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))