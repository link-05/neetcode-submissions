class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def sets(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            sets(i+1, subset)
            subset.pop()
            # Exclude skips all dup
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            sets(i+1, subset)
        sets(0, [])
        return res