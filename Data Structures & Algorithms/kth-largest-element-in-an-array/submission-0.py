class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        val = 0
        for i in range(k):
            val = heapq.heappop(nums)
        return -val