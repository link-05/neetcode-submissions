class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        # These two pointers are on the two edges
        minVal = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                if minVal > nums[left]:
                    minVal = nums[left]
            else:
                if minVal > nums[right]:
                    minVal = nums[right]
            left+=1
            right-=1
        return minVal