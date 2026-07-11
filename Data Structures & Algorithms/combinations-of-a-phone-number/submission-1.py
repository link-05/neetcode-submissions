class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        numToList = {"2":["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        def dfs(i, sets, letters):
            if i > len(digits):
                return
            if len(digits) == len(sets):
                res.append("".join(sets))
                return
            cand = letters[i]
            for c in cand:
                sets.append(c)
                dfs(i+1, sets, letters)
                sets.pop()
        cands = []
        for i in range(len(digits)):
            cand = numToList[digits[i:i+1]]
            cands.append(cand)
        dfs(0, [], cands)
        return res


