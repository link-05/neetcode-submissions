class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(sets):
            if len(sets) == len(nums):
                res.append(sets.copy())
                return
            for j in range(len(nums)):
                if nums[j] in sets:
                    continue
                sets.append(nums[j])
                backtrack(sets)
                sets.pop()
        backtrack([])
        return res