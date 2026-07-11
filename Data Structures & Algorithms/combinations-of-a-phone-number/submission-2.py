class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        numToList = {"2":"abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        def dfs(i, s):
            if i > len(digits):
                return
            if len(digits) == len(s):
                res.append(s)
                return
            for c in numToList[digits[i]]:
                dfs(i+1, s + c)
        dfs(0, "")
        return res


