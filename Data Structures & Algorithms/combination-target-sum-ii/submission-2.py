class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort to allow pruning dup
        candidates.sort()
        # Results
        res = []
        # ith value, subset, sums at target
        def dfs(i, sets, sums):  
            # base case for appending    
            if sums == target:
                res.append(sets.copy())
                return
            # impossible case return
            if sums > target:
                return
            # Test all non duplicate combinations from i to n
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # Add candidate to sets
                sets.append(candidates[j])
                # Recurse
                dfs(j+1, sets, sums + candidates[j])
                # prepare for next iteration by popping
                sets.pop()
        dfs(0, [], 0)
        return res