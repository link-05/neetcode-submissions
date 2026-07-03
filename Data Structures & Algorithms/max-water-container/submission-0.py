class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        mVal = (high - low) * min(heights[low], heights[high])
        while low < high:
            water =  (high - low) * min(heights[low], heights[high])
            if water > mVal:
                mVal = water
            if heights[low] < heights[high]:
                low+=1
            else:
                high-=1
        return mVal