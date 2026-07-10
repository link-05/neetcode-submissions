class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, sets, sums):      
            if sums == 0:
                res.append(sets.copy())
                return
            if sums < 0:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # Call every possible unique set
                sets.append(candidates[j])
                dfs(j+1, sets, sums - candidates[j])
                sets.pop()
        dfs(0, [], target)
        return res