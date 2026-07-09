class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sets = []
        def dfs(i):
            # If out of bound 
            if i >= len(nums):
                res.append(sets.copy())
                return
            # Insert target
            sets.append(nums[i])
            # Include and not include recursion
            dfs(i+1)
            sets.pop()
            dfs(i+1)
        dfs(0)
        return res
        