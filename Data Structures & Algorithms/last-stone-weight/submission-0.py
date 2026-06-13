class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heap = stones
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if x == y:
                continue
            heapq.heappush(heap, (x - y)* -1)
        if len(heap) == 1:
            return heap[0] * -1
        else:
            return 0
        