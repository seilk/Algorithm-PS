class Solution :

	def minimumTime(self, time: List[int], totalTrips: int) -> int :

		def findTrips(mid) :
			tot = 0
			for t in time :
				tot += mid//t
			return tot

		MAX = 10**14  # key

		left = 1
		right = MAX
		ans = MAX
		while left <= right :
			mid = (left+right)//2
			trips = findTrips(mid)
			if trips < totalTrips :
				left = mid+1
			else :
				ans = mid
				right = mid-1

		return ans