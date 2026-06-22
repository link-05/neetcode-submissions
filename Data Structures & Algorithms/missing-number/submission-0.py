class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = 0
        for i in range(len(nums) + 1):
            sums += i
        for num in nums:
            sums -= num
        return sums