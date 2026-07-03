class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search test 
        # for eating rate
        low = 1
        high = max(piles)
        # 1 bite per pile is high
        minVal = high
        # Normal binary search
        while low <= high:
            k = (high + low) // 2

            # Setup counter to find how many hours per pile 
            total = 0
            for p in piles:
                total += math.ceil(p/k)
            # Compare counter with h
            if total <= h:
                minVal = k
                high = k - 1
            else:
                low = k + 1
        return minVal