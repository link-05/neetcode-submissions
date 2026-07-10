# Boolean array way
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Check for whether element used yet
        cand = [False] * len(nums)
        def backtrack(sets):
            # Full perm
            if len(sets) == len(nums):
                res.append(sets.copy())
                return
            # Call every possible combination except used combo
            for j in range(len(nums)):
                # Base - used
                if cand[j]:
                    continue
                # Mark and append
                cand[j] = True
                sets.append(nums[j])
                # Recurse
                backtrack(sets)
                # Pop and unmark
                sets.pop()
                cand[j] = False
        backtrack([])
        return res
