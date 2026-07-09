class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort() Useful for certain pruning
        ret = []

        def dfs(i, sets):
            # check case
            sums = sum(sets.copy())
            if sums == target:
                ret.append(sets.copy())
                return
            # Base case
            if sums > target or i >= len(nums):
                return
            # candidate case
            sets.append(nums[i])
            # Allow choosing same number infinite time
            dfs(i, sets)
            # Backtrack and skip the nums at ith value
            sets.pop()
            dfs(i+1, sets)
        dfs(0, [])
        return ret

