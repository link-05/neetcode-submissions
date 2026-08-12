class Solution:
    def trap(self, height: List[int]) -> int:
        # array of non negative integers
        # height revealing elevation sort of like buildings 
        # every value in the array represents the height of a width 1 bar
        # The maximum area of water that can be trapped between the bars
        # 1 0 1 -> 1
        # 0 0 1 -> 0
        # 2 0 1 -> 1
        # 2 0 2 -> 2
        # Cases left wall is less than right, move from right to left, else left to right
        res = 0
        l = 0 # Smallest possible index
        r = len(height) - 1 # Largest possible index
        # The actual values, to calculate largest amount of rainwater
        leftMax = height[0] 
        rightMax = height[len(height) - 1] 
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l]) # update to greater of 2
                res += leftMax - height[l] # If updated then = 0 else the diff
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] # The difference of current and the wall
        return res
