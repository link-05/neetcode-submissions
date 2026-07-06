class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            heapq.heapify_max(nums)
            outcome = heapq.heappop_max(nums)
        return outcome